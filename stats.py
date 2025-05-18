def get_book_text(path_to_file):
   with open(path_to_file) as f:
      file_contents = f.read()
      
   return file_contents
    

def get_numbers_of_words(files_contents):
   count_of_words = 0
   words = files_contents.split()
   for word in words:
      
      count_of_words += 1
    
   return count_of_words

def get_numbers_of_character(files_contents):
   dict_count = {}
   for word in files_contents:
      word_lower = word.lower()
      if word_lower in dict_count:
         dict_count[word_lower] += 1
      else:
         dict_count[word_lower] = 1
        
   return dict_count

def sorted_dict(dict_count):
   characters = []
   for key,value in dict_count.items():
      characters.append({"name":key,"num":value})
   
   characters.sort(key=lambda x: x["num"], reverse=True)
   
   return characters
   
   
   




      
   

   
   
   

         
         


   
