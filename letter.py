letter = ''' Dear <| NAME |>

     You Are Selected !
                
     Date :<| DATE |>'''
print(letter)
 aaa=input(" Enter Your Name :")
 bbb=input(" Enter Date :")
 letter=(letter.replace("NAME",aaa))
 letter=(letter.replace("DATE",bbb))
 print(letter)