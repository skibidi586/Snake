import com.googlecode.lanterna.TerminalPosition;
import com.googlecode.lanterna.input.KeyStroke;
import com.googlecode.lanterna.screen.*;
import com.googlecode.lanterna.terminal.DefaultTerminalFactory;
import com.googlecode.lanterna.graphics.TextGraphics;
import com.googlecode.lanterna.TerminalSize;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

public class Snack {
	public static void main(String[] args) throws Exception {
		Screen screen = new DefaultTerminalFactory().createScreen();
		screen.startScreen();

		screen.setCursorPosition(null);

		TextGraphics g = screen.newTextGraphics();
		TerminalSize size = screen.getTerminalSize();

		boolean grow = false;

		int height = size.getRows();
		int width = size.getColumns();
		int maxY = height - 1;
		int maxX = width - 1;
		int playableArea = width * height;

		int dx = 1;
		int dy = 0;

		ArrayList<TerminalPosition> head = new ArrayList<>(List.of(
			new TerminalPosition(width / 2 + 1, height / 2 + 1),
			new TerminalPosition(width / 2, height / 2 + 1),
			new TerminalPosition(width / 2 - 1, height / 2 + 1)
		));

		ArrayList<Apple> appies = new ArrayList<>();

		for (int i = 0; i < 15; i++) {
			appies.add(
				new Apple(
					(int)(Math.random() * maxX),
					(int)(Math.random() * maxY)
				)
			);
		}

		for (int y = 0; y < maxY; y++) {
			for (int x = 0; x < maxX; x++) {
				g.putString(x, y, ".");
			}
		}

		while (true) {
			screen.clear();
			TerminalPosition face = head.get(0);

			KeyStroke key = screen.pollInput();
			if (key != null) {
				switch (key.getKeyType()) {
					case ArrowUp -> { dx = 0; dy = -1; }
					case ArrowLeft -> { dx = -1; dy = 0; }
					case ArrowDown -> { dx = 0; dy = 1; }
					case ArrowRight -> { dx = 1; dy = 0; }
					case Character -> {
						char c = key.getCharacter();

						switch (c) {
							case 'w' -> { dx = 0; dy = -1; }
							case 'a' -> { dx = -1; dy = 0; }
							case 's' -> { dx = 0; dy = 1; }
							case 'd' -> { dx = 1; dy = 0; }
							case 'e' -> System.exit(0);
						}
					}
				}
			}

			int newX = face.getColumn() + dx;
			int newY = face.getRow() + dy;
			TerminalPosition newHead = new TerminalPosition(newX, newY);

			if (newY < 0 || newY >= height || newX < 0 || newX >= width) {
				screen.clear();
				g.putString(0, 0, "Game Over!!");
				screen.refresh();
				Thread.sleep(150);
				System.exit(0);
			}

			for (int i = 0; i < head.size() - 1; i++) {
				if (head.get(i).equals(newHead)) {
					screen.clear();
					g.putString(0, 0, "Game Over!!");
					screen.refresh();
					Thread.sleep(150);
					System.exit(0);
				}
			}

			Set<TerminalPosition> occupied = new HashSet<>(head);
			int freeCells = playableArea - occupied.size();

			if (freeCells == 0) {
				screen.clear();
				g.putString(0, 0, "You win!!");
				screen.refresh();
				Thread.sleep(150);
				System.exit(0);
			}

			for (Apple a : appies) {
				if (newX == a.x && newY == a.y) {
					grow = true;
					TerminalPosition appyPos = respawnApple(width, height, head);

					a.x = appyPos.getColumn();
					a.y = appyPos.getRow();
				}
			}

			head.add(0, newHead);

			if (!grow) {
				head.remove(head.size() - 1);
			} else {
				grow = false;
			}

			for (Apple a : appies) {
				g.putString(a.x, a.y, "o");
			}
			
			render(head, g);

			screen.refresh();
			Thread.sleep(150);
		}
	}

	static void render(ArrayList<TerminalPosition> head, TextGraphics g) {
		for (TerminalPosition pos : head) {
			int x = pos.getColumn();
			int y = pos.getRow();
			g.putString(x, y, "#");
		}
	}

	static TerminalPosition respawnApple(int width, int height, ArrayList<TerminalPosition> head) {
		while (true) {
			int x = (int)(Math.random() * width);
			int y = (int)(Math.random() * height);

			boolean valid = true;

			for (TerminalPosition pos : head) {
				if (pos.getColumn() == x && pos.getRow() == y) {
					valid = false;
					break;
				}
			}

			if (valid) {
				return new TerminalPosition(x, y);
			}
		}
	}
}

class Apple {
	int x;
	int y;

	Apple(int y, int x) {
		this.x = x;
		this.y = y;
	}
}
