class PhoneBook():
    def __init__(self, file_path: str):
        self.file_path = file_path  # File name entered by user
        self.accepted_sort_ordering = {"Ascending", "Descending"}
        self.accepted_sort_criteria = {"Name", "Surname", "PhoneNumberCode"}

    def read_records(self) -> None:
        """
        Read records from file with predefined structure and
        calling sort_records function to sort it.
        """
        with open(f"./{self.file_path}", "rt") as records:
            file_structure = [record.split() for record in records]
        self.sort_records(file_structure)

    def select_sort_order(self) -> str:
        """
        Get input from user to select sort order

        Returns
        ---------
        string
        """
        return input(
            "Please choose an ordering to sort "
            "(“Ascending” or “Descending”): "
        )

    def select_sort_criteria(self) -> str:
        """
        Get input from user to select sort criteria

        Returns
        ---------
        string
        """
        return input(
            "“Please choose criteria (“Name”, “Surname” or "
            "“PhoneNumberCode”): "
        )

    def sort_records(self, file_structure: list) -> None:
        """
        Sort records from received argument
        depends on user selected sort order and criteria

        Parameter
        ---------
        file_structure : list
            Sorted file records in list structure.
        """
        while True:
            selected_sort_ordering = self.select_sort_order()
            if selected_sort_ordering in self.accepted_sort_ordering:
                while True:
                    selected_sort_criteria = self.select_sort_criteria()
                    if selected_sort_criteria in self.accepted_sort_criteria:
                        sort_criteria = (
                            0 if selected_sort_criteria == "Name"
                            else 1 if selected_sort_criteria == "Surname"
                            else 3
                        )
                        sort_order = selected_sort_ordering != "Ascending"
                        records_with_surname = [
                            record for record in file_structure
                            if len(record) == 4
                        ]
                        records_without_surname = [
                            record for record in file_structure
                            if len(record) == 3
                        ]
                        if sort_criteria == 1:
                            sorted_structure = sorted(
                                records_with_surname,
                                key=lambda index: (
                                    index[sort_criteria]
                                ),
                                reverse=sort_order
                            )
                            sorted_structure.extend(
                                sorted(
                                    records_without_surname,
                                    reverse=sort_order
                                )
                            )
                        else:
                            sorted_structure = sorted(
                                file_structure,
                                key=lambda index: (
                                    index[sort_criteria-1]
                                    if sort_criteria == 3
                                    and len(index) == 3
                                    else index[sort_criteria][:3]
                                    if sort_criteria == 3
                                    else index[sort_criteria]
                                ),
                                reverse=sort_order
                            )
                        self.show_sorted_file_structure(sorted_structure)
                        break
                    else:
                        print("You can choose criteria only "
                              "with predefined words.")
                break
            else:
                print("You can choose an ordering only with predefined words.")

    def show_sorted_file_structure(self, sorted_structure: list) -> None:
        """
        Show sorted_structure line by line.
        Show validation results line by line.

        Parameter
        ---------
        sorted_structure : list
            Sorted records in list structure.
        """
        print("File Structure:")
        for structure in sorted_structure:
            print(" ".join(structure))
        print("\nValidations:")
        self.validate_records(sorted_structure)

    def records_validation_message(
        self,
        separator: bool = False,
        phone_number: bool = False
    ) -> str:
        """
        Show validation errors in messages.

        Parameter
        ---------
        separator : bool
        phone_number: bool
        """
        if separator:
            if phone_number:
                return ("Phone number should be with 9 digits, "
                        "the separator should be `: ` or `-`.")
            else:
                return "Separator should be `:` or `-`."
        return "Phone number should be with 9 digits."

    def validate_records(self, sorted_structure: list) -> None:
        """
        Validate records of sorted file structure and
        calling records_validation_message function
        to display validation errors line by line.

        Parameter
        ---------
        sorted_structure : list
            Sorted records in list structure.
        """
        for index, line in enumerate(sorted_structure):
            separator = 2 if len(line) == 4 else 1
            phone_number = 3 if len(line) == 4 else 2
            if line[separator] not in ":-" and len(line[phone_number]) != 9:
                print(f"Line {index+1}: ",
                      self.records_validation_message(True, True))
            elif line[separator] not in ":-":
                print(f"Line {index+1}: ",
                      self.records_validation_message(True))
            elif len(line[phone_number]) != 9:
                print(f"Line {index+1}: ",
                      self.records_validation_message(False, True))


while True:
    file_path = input("Please write file path (“records.txt”): ")
    if file_path == "records.txt":
        phone_book = PhoneBook(file_path)
        phone_book.read_records()
        break
    else:
        print("Please write this file path (“records.txt”)")
