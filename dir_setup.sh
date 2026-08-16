for item in \
  "part06-01_largest_number largest_number" \
  "part06-02_fruit_market fruit_market" \
  "part06-03_matrix matrix" \
  "part06-04_course_grading_part_1 course_grading_part_1" \
  "part06-05_course_grading_part_2 course_grading_part_2" \
  "part06-06_course_grading_part_3 course_grading_part_3" \
  "part06-07_spellchecker spellchecker" \
  "part06-08_recipe_search recipe_search" \
  "part06-09_city_bikes city_bikes" \
  "part06-10_inscription inscription" \
  "part06-11_diary diary" \
  "part06-12_filtering_file_contents filtering_file_contents" \
  "part06-13_store_personal_data store_personal_data" \
  "part06-14_course_grading_part_4 course_grading_part_4" \
  "part06-15_word_search word_search" \
  "part06-16_dictionary_file dictionary_file" \
  "part06-17_read_input read_input" \
  "part06-18_parameter_validation parameter_validation" \
  "part06-19_incorrect_lottery_numbers incorrect_lottery_numbers"; do
    set -- $item
    mkdir -p "$1/src" && touch "$1/src/$2.py"
done
