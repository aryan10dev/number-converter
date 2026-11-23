#!/usr/bin/env python3
"""
Number Base Converter + Basic Logic Gates
Simple tool for digital electronics / computer fundamentals practice.
"""

def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))

def binary_to_decimal(b):
    return int(b, 2)

def decimal_to_hex(n):
    return hex(n)[2:].upper()

def hex_to_decimal(h):
    return int(h, 16)

def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return 1 - a

def show_truth_table():
    print("\n--- Basic Logic Gates Truth Table ---")
    print("A B | AND OR  NOT(A)")
    print("----|-------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"{a} {b} |  {and_gate(a,b)}   {or_gate(a,b)}    {not_gate(a)}")

def main():
    while True:
        print("\n===== Number Converter & Logic Gates =====")
        print("1. Decimal → Binary")
        print("2. Binary → Decimal")
        print("3. Decimal → Hex")
        print("4. Hex → Decimal")
        print("5. Show Logic Gates Truth Table")
        print("6. Exit")
        
        choice = input("\nChoose (1-6): ").strip()
        
        if choice == "1":
            try:
                n = int(input("Enter decimal number: "))
                print(f"Binary: {decimal_to_binary(n)}")
            except:
                print("Invalid input.")
        elif choice == "2":
            b = input("Enter binary number: ").strip()
            try:
                print(f"Decimal: {binary_to_decimal(b)}")
            except:
                print("Invalid binary.")
        elif choice == "3":
            try:
                n = int(input("Enter decimal: "))
                print(f"Hex: {decimal_to_hex(n)}")
            except:
                print("Invalid input.")
        elif choice == "4":
            h = input("Enter hex (e.g. 1A): ").strip()
            try:
                print(f"Decimal: {hex_to_decimal(h)}")
            except:
                print("Invalid hex.")
        elif choice == "5":
            show_truth_table()
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
