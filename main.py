import sys

from stats import get_book_text, get_numbers_of_words, get_numbers_of_character, sorted_dict


def main():
   if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   
   else:
      file_contents = get_book_text(f"{sys.argv[1]}")
      count_of_words = get_numbers_of_words(file_contents)
      count_of_character = get_numbers_of_character(file_contents)

      list_sorted = sorted_dict(count_of_character)
   
      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {sys.argv[1]}...")
      print("----------- Word Count ----------")
      print(f"Found {count_of_words} total words")
      print("--------- Character Count -------")
      for list in list_sorted:
         if list["name"].isalpha() == True:
          print(f"{list["name"]}: {list["num"]}")
   
      print("============= END ===============")
   


main()
