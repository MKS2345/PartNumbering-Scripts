import argparse
import time
import pyautogui


def main():
    parser = argparse.ArgumentParser(
        description="Auto-type sequential IDs with Shift+Enter"
    )

    parser.add_argument(
        "--prefix",
        required=True,
        help="Prefix (example: 502-C0-P)"
    )

    parser.add_argument(
        "--start",
        type=int,
        required=True,
        help="Start number (example: 1 for 001)"
    )

    parser.add_argument(
        "--end",
        type=int,
        required=True,
        help="End number (example: 14 for 014)"
    )

    parser.add_argument(
        "--pad",
        type=int,
        default=3,
        help="Zero padding length (default: 3 → 001)"
    )

    parser.add_argument(
        "--delay",
        type=int,
        default=5,
        help="Seconds before typing starts (default: 5)"
    )

    args = parser.parse_args()

    print(f"Starting in {args.delay} seconds...")
    time.sleep(args.delay)

    for i in range(args.start, args.end + 1):
        num = str(i).zfill(args.pad)
        text = f"{args.prefix}{num}"

        pyautogui.write(text)
        pyautogui.hotkey("shift", "enter")

        time.sleep(0.1)

    print("Done.")


if __name__ == "__main__":
    main()
