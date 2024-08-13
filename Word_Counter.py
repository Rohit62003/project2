
#  Function is used to count the number of words in the input. 
def count_words(input_text):
    words = input_text.split() #Split the input text by spaces to get the words
    # Return the number of words
    return len(words)


#Main function to taking user input and display output.
def main():
    try:
        #  taking user input 
        user_input = input("Enter a sentence or paragraph: ")
        
        # Check the input is empty
        if not user_input.strip():
            raise ValueError("Please enter the sentence or paragraph.")
        
        # Count the number of words in the input
        word_count = count_words(user_input)
        
        # Print the word count to the console
        print(f"The number of words in the input is: {word_count}")
    
    except ValueError as e:
        # Handle empty input error
        print(e)

if __name__ == "__main__":
    main()


