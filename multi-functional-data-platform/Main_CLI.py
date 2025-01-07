# --- Main CLI ---
def main():
    print("Airport Queue Control System")
    while True:
        print("\n1. Graph Operations")
        print("2. Stack/Queue Operations")
        print("3. Sorting Operations")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Graph Operations")
            edges = [("Check-in", "Security"), ("Security", "Boarding")]
            try:
                graph = create_dag(edges)
                order = topological_sort(graph)
                print("Topological Order:", order)
            except ValueError as e:
                print(e)

        elif choice == "2":
            print("Stack/Queue Operations")
            stack = TwoStacksOneArray(10)
            stack.push1(5)
            stack.push2(10)
            print("Stack 1 Pop:", stack.pop1())
            print("Stack 2 Pop:", stack.pop2())

        elif choice == "3":
            print("Sorting Operations")
            arr = [3, 6, 8, 10, 1, 2, 1]
            print("Original Array:", arr)
            sorted_arr = quick_sort(arr)
            print("Sorted Array (Quick Sort):", sorted_arr)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
