import argparse
import time
import pyautogui


def main():
    parser = argparse.ArgumentParser(
        description="Automate clicking, typing, and part entry"
    )

    parser.add_argument("--prefix", required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)

    parser.add_argument("--pad", type=int, default=3)
    parser.add_argument("--delay", type=int, default=5)

    parser.add_argument(
        "--move",
        type=int,
        default=50,
        help="Pixels to move down each cycle"
    )

    parser.add_argument(
        "--step-delay",
        type=float,
        default=0.1,
        help="Delay between actions (seconds)"
    )

    args = parser.parse_args()

    print(f"Starting in {args.delay} seconds...")
    time.sleep(args.delay)

    for i in range(args.start, args.end + 1):

        # 1. Click
        pyautogui.click()
        time.sleep(args.step_delay)

        # 2. Press space
        pyautogui.press("space")
        time.sleep(args.step_delay)

        # 3. Click
        pyautogui.click()
        time.sleep(args.step_delay)

        # 4. Press Shift+N
        pyautogui.hotkey("shift", "n")
        time.sleep(args.step_delay)

        # 5. Move down
        pyautogui.moveRel(0, args.move)
        time.sleep(args.step_delay)

        # 6. Type part number
        num = str(i).zfill(args.pad)
        part = f"{args.prefix}{num}"

        pyautogui.write(part)
        time.sleep(args.step_delay)

    print("Done.")


if __name__ == "__main__":
    main()
