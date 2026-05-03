"""Smart Room Light Controller

Console prototype for the EEE120 final project.

The decision logic follows the assignment:
- If energy saving mode is OFF: light = (person_detected AND room_is_dark) OR manual_switch
- If energy saving mode is ON: light = person_detected

The program also prints the decision table and can run a few built-in checks.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


def gate_and(a: bool, b: bool) -> bool:
    return a and b


def gate_or(a: bool, b: bool) -> bool:
    return a or b


def gate_not(a: bool) -> bool:
    return not a


@dataclass(frozen=True)
class Decision:
    light_on: bool
    mode: str
    explanation: str


def decide_light(
    person_detected: bool,
    room_is_dark: bool,
    manual_switch_on: bool,
    energy_saving_mode_on: bool,
) -> Decision:
    """Evaluate the light using gate-style boolean logic."""

    person_and_dark = gate_and(person_detected, room_is_dark)

    not_energy_saving = gate_not(energy_saving_mode_on)
    person_in_energy_mode = gate_and(person_detected, energy_saving_mode_on)
    person_dark_normal_mode = gate_and(person_and_dark, not_energy_saving)
    manual_normal_mode = gate_and(manual_switch_on, not_energy_saving)

    light_on = gate_or(
        gate_or(person_dark_normal_mode, manual_normal_mode),
        person_in_energy_mode,
    )

    if energy_saving_mode_on:
        mode = "Energy saving mode"
        explanation = (
            "Energy saving mode is ON, so the circuit uses person detection as "
            "the enabling path and blocks the manual switch path."
        )
    else:
        mode = "Normal mode"
        explanation = (
            "Energy saving mode is OFF, so the circuit allows either the "
            "person-and-dark path or the manual-switch path."
        )

    return Decision(light_on=light_on, mode=mode, explanation=explanation)


def bit(value: bool) -> str:
    return "1" if value else "0"


def yn(value: bool) -> str:
    return "YES" if value else "NO"


def prompt_bool(label: str) -> bool:
    while True:
        answer = input(f"{label} [y/n, 1/0]: ").strip().lower()
        if answer in {"y", "yes", "1", "true", "t"}:
            return True
        if answer in {"n", "no", "0", "false", "f"}:
            return False
        print("Please enter y/n or 1/0.")


def print_single_result(
    person_detected: bool,
    room_is_dark: bool,
    manual_switch_on: bool,
    energy_saving_mode_on: bool,
) -> None:
    decision = decide_light(
        person_detected=person_detected,
        room_is_dark=room_is_dark,
        manual_switch_on=manual_switch_on,
        energy_saving_mode_on=energy_saving_mode_on,
    )

    print("\nDecision Summary")
    print("-" * 16)
    print(f"Person detected      : {yn(person_detected)}")
    print(f"Room is dark         : {yn(room_is_dark)}")
    print(f"Manual switch ON     : {yn(manual_switch_on)}")
    print(f"Energy saving mode ON: {yn(energy_saving_mode_on)}")
    print(f"Mode                 : {decision.mode}")
    print(f"Light output         : {'ON' if decision.light_on else 'OFF'}")
    print(f"Reason               : {decision.explanation}")


def print_truth_table() -> None:
    headers = [
        "P",
        "D",
        "M",
        "E",
        "~E",
        "P AND D",
        "(P AND D)&~E",
        "M&~E",
        "P&E",
        "LIGHT",
    ]
    widths = [5, 5, 5, 5, 5, 10, 12, 8, 6]

    def row(values: list[str]) -> str:
        return " | ".join(value.ljust(width) for value, width in zip(values, widths))

    print("\nDecision Table")
    print("-" * 78)
    print(row(headers))
    print("-" * 78)
    for person_detected, room_is_dark, manual_switch_on, energy_saving_mode_on in product([False, True], repeat=4):
        decision = decide_light(
            person_detected=person_detected,
            room_is_dark=room_is_dark,
            manual_switch_on=manual_switch_on,
            energy_saving_mode_on=energy_saving_mode_on,
        )
        person_and_dark = gate_and(person_detected, room_is_dark)
        not_energy_saving = gate_not(energy_saving_mode_on)
        person_dark_normal_mode = gate_and(person_and_dark, not_energy_saving)
        manual_normal_mode = gate_and(manual_switch_on, not_energy_saving)
        person_in_energy_mode = gate_and(person_detected, energy_saving_mode_on)
        print(
            row(
                [
                    bit(person_detected),
                    bit(room_is_dark),
                    bit(manual_switch_on),
                    bit(energy_saving_mode_on),
                    bit(not_energy_saving),
                    bit(person_and_dark),
                    bit(person_dark_normal_mode),
                    bit(manual_normal_mode),
                    bit(person_in_energy_mode),
                    bit(decision.light_on),
                ]
            )
        )


def run_self_tests() -> None:
    cases = [
        (False, False, False, False, False),
        (True, True, False, False, True),
        (True, False, False, False, False),
        (False, True, True, False, True),
        (False, False, True, True, False),
        (True, False, False, True, True),
        (False, True, True, True, False),
    ]

    print("\nRunning self-tests")
    print("-" * 18)
    passed = 0
    for index, (person_detected, room_is_dark, manual_switch_on, energy_saving_mode_on, expected) in enumerate(cases, start=1):
        decision = decide_light(
            person_detected=person_detected,
            room_is_dark=room_is_dark,
            manual_switch_on=manual_switch_on,
            energy_saving_mode_on=energy_saving_mode_on,
        )
        ok = decision.light_on == expected
        passed += int(ok)
        status = "PASS" if ok else "FAIL"
        print(
            f"Case {index}: P={bit(person_detected)} D={bit(room_is_dark)} "
            f"M={bit(manual_switch_on)} E={bit(energy_saving_mode_on)} -> "
            f"{bit(decision.light_on)} expected {bit(expected)} [{status}]"
        )

    print(f"\n{passed}/{len(cases)} tests passed.")


def interactive_mode() -> None:
    print("Smart Room Light Controller")
    print("===========================")
    print("This program evaluates a real boolean decision circuit for the assignment.\n")

    while True:
        print("Menu")
        print("1. Evaluate one room scenario")
        print("2. Show decision table")
        print("3. Run self-tests")
        print("4. Exit")
        choice = input("Select an option [1-4]: ").strip()

        if choice == "1":
            person_detected = prompt_bool("Person detected")
            room_is_dark = prompt_bool("Room is dark")
            manual_switch_on = prompt_bool("Manual switch ON")
            energy_saving_mode_on = prompt_bool("Energy saving mode ON")
            print_single_result(
                person_detected=person_detected,
                room_is_dark=room_is_dark,
                manual_switch_on=manual_switch_on,
                energy_saving_mode_on=energy_saving_mode_on,
            )
            print()
        elif choice == "2":
            print_truth_table()
            print()
        elif choice == "3":
            run_self_tests()
            print()
        elif choice == "4":
            print("Exiting.")
            return
        else:
            print("Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    interactive_mode()