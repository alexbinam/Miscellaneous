

#In this assignment you will check if HTML (a language for making web pages) is valid or not based on highly simplified rules.

#You are going to compare closing and opening tags and make sure they match and come in the right order. The rules for our simple HTML are as follows:

#Opening tags are of the form <tag_name>
#Closing tags are of the form </tag_name>
#Every opening tag must be followed by zero or more matching opening and closing tag pairs or a matching closing tag.
#There must be an equal number of opening and closing tags
#There can be text at any point outside of the tags

example_set = ['''<a><b><c></c></b></a>''',
 '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
 '''<foo><bar></bop></bar></foo>''',
 '''<foo><bar></bar></foo></foo>''',
 '''<foo><bar></foo></bar>''']
#import pandas as pd
import re

def return_opening_tags(test_strings):
    opening_tag_re = re.compile(r'<[a-zA-Z]+>')
    opening_tags = [re.findall(opening_tag_re, x) for x in test_strings]
    
    return(opening_tags)
    
def return_closing_tags(test_strings):
    closing_tag_re = re.compile(r'</[a-zA-Z]+>')
    closing_tags = [re.findall(closing_tag_re, x) for x in test_strings]
    
    return(closing_tags)


def remove_slash(test_strings):
  html_list = []
  all_tags_re = re.compile(r'</*[a-zA-Z]+>')
  all_tags = [re.findall(all_tags_re, x) for x in test_strings]
  for i in all_tags:
    html_list.append(i)
  for i in range(len(html_list)):
    html_list[i] = [s.replace('/', '') for s in html_list[i]]
  return(html_list)



def valid_html(test_strings):
    result = []
    new_result = []
    is_valid = True
    new_test_strings = remove_slash(test_strings)
    opening_tags = return_opening_tags(test_strings)
    closing_tags = return_closing_tags(test_strings) 
    for i in range(len(new_test_strings)):
      if len(closing_tags[i]) != len(opening_tags[i]):
        is_valid = False
        result.append(tuple((test_strings[i], is_valid)))
      else:
        position = len(new_test_strings[i])-1
        for index, x in enumerate(new_test_strings[i]):
          if index == position:
            is_valid = False
            result.append(tuple((test_strings[i], is_valid)))
          elif x == new_test_strings[i][position]:
            is_valid = True
            result.append(tuple((test_strings[i], is_valid)))
            position -=1
          else:
            is_valid = False 
    result = list(set(result))
    result_part = [x[0] for x in result]
    for i in range(len(result)):
       for i in range(len(result_part)):
           if result_part[i-1] != result_part[i]:
            new_result.append(result[i])
    return(set(new_result))







