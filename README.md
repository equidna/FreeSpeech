<h1>simplecsvtools</h1>
  
  After scraping a website I would usually find the need to do some operations over the resulting csv file, eventually I took those scripts, cleaned the code and created a python package.
  Has of now there are only 4 functions:
  <ul>
    <li>count_rows</li>
    <li>edit_columns</li>
    <li>join_files</li>
    <li>split_file</li>
  </ul>
  
  
<h2>count_rows</h2>
  
  For counting the number of rows in a csv file. It only takes one argument: the name of the file in question.
  
  ex:
  
  <code>
  row_number = count_rows("./dir/filename.csv")
  </code>
  
  
<h2>edit_columns</h2>
  
  For batch replacement of characters in columns belonging to a csv file. It has 3 parameters:
  <ul>
    <li>files - a list with 2 elements: the first element is the input filename and the second element is the output filename</li>
    <li>changing_indexes - a list of indexes of the columns to be changed</li>
    <li>items - a list with 2 elements: the first element is a list of strings that need to be changed and the the second element is a list of corresponding strings that are going to replace the old strings. The list of old strings and new strings need to be of the same size</li>
  </ul>
  
  ex:
  
  <code>input_file = "file.csv"</code><br>
  <code>output_file = "new_file.csv"</code><br>
  <code>changing_indexes = [0, 1, 3]</code><br>
  <code>old_items = [":", "is"]</code><br>
  <code>new_items = ["&", "was"]</code><br>
  <code>files = [input_file, output_file]</code><br>
  <code>items = [old_items, new_items]</code><br>
  <code>edit_columns(files, changing_indexes, items)</code>
  
  
<h2>join_files</h2>
  
  This function assumes you have a a sequence of files, you want to join, whose filenames end in a number sequence ranging from 00 to 99 (ex: file_00.csv, file_01.csv, file_02.csv, ...). It has 2 parameters:
  <ul>
    <li>filename - the filename without the extension</li>
    <li>limits - A list whose first argument is the lower limit for the sequence of numbers at the end of the filename and the second is the upper limit</li>
  </ul>
  
  ex:
  
  <code>
  join_files("file", [2, 5])
  </code>
  
  
<h2>split_file</h2>
  
  This function tries to split a large csv file into small ones with equal number of rows. It has 2 parameters:
  <ul>
    <li>filename - the filename without the extension</li>
    <li>divisor - the number of rows the files are going to be broken into</li>
  </ul>
  
  ex:
  
  <code>
  split_file("file", 999)
  </code>


<h2>delete_columns</h2>
  
  This function tries to remove selected columns from a csv file. It has 3 parameters:
  <ul>
    <li>input_file - the input file</li>
    <li>output_file - the output file with the columns removed</li>
    <li>columns - the list of indexes of the columns to be removed</li>
  </ul>
  
  ex:
  
  <code>
  delete_columns("file.csv", "new_file.csv", [2, 3, 5])
  </code>


<h2>remove_duplicates</h2>
  
  Removes the duplicate rows from a csv file. It has 3 parameters:
  <ul>
    <li>input_file - the input file</li>
    <li>output_file - the output file with the duplicates removed</li>
    <li>column_id - the column where should be unique values</li>
  </ul>
  
  ex:
  
  <code>
  remove_duplicates("file.csv", "new_file.csv", 2)
  </code>
