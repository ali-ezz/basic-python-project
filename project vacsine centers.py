#admin info:
name1='a'
id1='1'
email1='a'
password1='1'
#user info:
user_info=['name','email','password','national id','phone number']
user1=['a','a','1','1','1']
users=[]
users.insert(0,user_info)
users.insert(1,user1)
#Vaccination center
info=['name','adress','id']
cairo=['cairo','imbaba','123']
alex=['alex','houspital','456']
vecatine_centers=[]
vecatine_centers.insert(0,info)
vecatine_centers.insert(1,cairo)
vecatine_centers.insert(1,alex)
user_Reserve_vaccination=[]
###########counters#############
counter1=0
counter2=0
counter3=0
counter4=0
#############vaccine typs##############
vaccine_typs_original=['moderna','pfizer','astrazeneca']
vaccine_typs=[]
vaccine_typs.extend(vaccine_typs_original)
user_date=[]
user_dates=[]
#########file paths#################
file_path1='Vaccination_center.txt'
file_path2='search_centers.txt'
file_path3='user_vcation.txt'
file_path4='user_dates.txt'
file_path5='vcation_typs.txt'
file_path6='users.txt'
##################admin or user login#################
while(True):
   print('welcome!')
   print('plaese inout a number for what do you want')
   z=raw_input('what are\n(1)an admin\n(2)a citzen\n(3)exit\n')
   if(z=='3'):
        print('good bye!')
        break
##################admin login##############
   elif(z=='1'):
       admin_name = raw_input('Please enter your name:')
       admin_id = raw_input('Please enter your id number:')
       admin_email = raw_input('Please enter your email:')
       admin_password = raw_input('Please enter your password number:')
       if admin_name == name1 and admin_id == id1 and admin_email == email1 and admin_password == password1:
##################admin center#################
        while(True):
         j=raw_input('what can we help you at sir\n(1)for editing the Vaccination center and Vaccination typs and search about a Vaccination center and users\n(2)for Accepting reservations and decide a date for user to get vaccination and see users data\n(3)exit\n')
         if(j=='1'):
           while(True):
            k=raw_input('do you want:\n(1)to add a Vaccination center\n(2)to delet a Vaccination center\n(3)to Search Vaccination center by its name\n(4)to add a Vaccination typs\n(5)to delet a Vaccination typs\n(6)for seeing users\n(7)exit\n')
            if(k=='7'):
              break
            elif(k=='6'):
               with open(file_path6,'w') as file:
                 for item in users:
                  file.write(str(item) + "\n")
            elif(k=='5'):
             vaccine_typs_input=raw_input('plaese enter the type of Vaccination\n')
             if(vaccine_typs_input not in vaccine_typs):
                print('the vaccine typs is not entered yet')
             else:
                vaccine_typs.remove(vaccine_typs_input)
                with open(file_path5,'w') as file:
                 for item in vaccine_typs:
                  file.write(str(item) + "\n")
                break
            elif(k=='4'):
              vaccine_typs_input=raw_input('plaese enter the type of Vaccination\n')
              if(vaccine_typs_input in vaccine_typs):
                print('the vaccine typs is alredy entered')
              else:
                vaccine_typs.append(vaccine_typs_input)
                with open(file_path5,'w') as file:
                 for item in vaccine_typs:
                  file.write(str(item) + "\n")
                break
            elif(k=='1'):
             while(True):
              l=[]
              vecatine_centers_name=raw_input('enter the Vaccination center name\n')
              l.insert(0,vecatine_centers_name)
              Vaccination_center_addres=raw_input('plaese enter the Vaccination center addres:')
              l.insert(1,Vaccination_center_addres)
              Vaccination_center_id=raw_input('plaese enter the Vaccination center id:')
              l.insert(3,Vaccination_center_id)
              all_is_old=True
              for sublist in vecatine_centers:
               if vecatine_centers_name  in sublist or Vaccination_center_addres  in sublist or Vaccination_center_id  in sublist:
                all_is_old = False
                break
              if(all_is_old):
               vecatine_centers.insert(1,l)
               with open(file_path1,'w') as file:
                for item in vecatine_centers:
                  file.write(str(item) + "\n")
               break
              else:
               print('the input is alryde added')
               break
            elif(k=='2'):
             while(True):
              i=raw_input('please enter the Vaccination center id\n')
              ######################
              filtered_list = [sublist for sublist in vecatine_centers if i not in sublist]
              with open(file_path1,'w') as file:
                 for sublist in filtered_list:
                   file.write(str(sublist) + "\n")
              print('vcation center deleted sucseed')
              break
             #####################
            elif(k=='3'):
             Z=raw_input('what is the name of Vaccination center do you want to Search\n')
             with open(file_path2, "w") as file:
              for sublist in vecatine_centers:
               if Z in sublist:
                file.write(str(sublist) + "\n")
              ##########################
              continue
            else:
             print('you enter wrong opration!!')
             continue
         elif(j=='2'):
          while(True):
             with open(file_path3,'w') as file:
              for item in user_Reserve_vaccination:
               file.write(str(item) + "\n")
             user_dechion=raw_input('do you want to\n(1)accept a Reserveion\n(2)decline a Reserveion\n(3)exit\n')
             if(user_dechion=='1'):
              user_date=[]
              admin_choise1=raw_input('plaese enter the id of the user Reserveion \n')
              for sublist in user_Reserve_vaccination:
                if admin_choise1 in sublist:
                  break
              else:
                print('the id did not rvrde a plase yet')
                break
              admin_choise2=raw_input('plese enter the date in(hour:minet/day/maunth/year)format\n')
              user_date.append(admin_choise1)
              user_date.append(admin_choise2)
              user_dates.append(user_date)
              with open(file_path4,'w') as file:
                file.write(str(user_date) + "\n")
              print(user_date)
              continue
             elif(user_dechion=='2'):
               user_delet_resirve=raw_input('enter the user national id you want to decline\n')
               for sublist in user_Reserve_vaccination:
                if user_delet_resirve in sublist:
                  user_Reserve_vaccination.remove(sublist)
                  print('reservction declined')
                  break
               else:
                print('the id did not risvrde a plase yet\n')
                break
             elif(user_dechion=='3'):
               break
             else:
               print('invaled input')
               continue
         elif(j=='3'):
          break
         else:
           print('invalid input')
           continue
       else:
         print('invalid input')
         continue
   elif(z=='2'):
     while(True):
      user_login_or_register=raw_input('do you want to\n(1)login\n(2)rigster\n(3)exit\n')
      if(user_login_or_register=='3'):
         break
      elif(user_login_or_register=='1'):
         user_name = raw_input('Please enter your name: ')
         user_email = raw_input('Please enter your email: ')
         user_password = raw_input('Please enter your password number: ')
         user_phone_number=raw_input('Please enter your phone number: ')
         user_national_id = raw_input('Please enter your National ID: ')
         user_login=[]
         user_login.append(user_name)
         user_login.append(user_email)
         user_login.append(user_password)
         user_login.append(user_phone_number)
         user_login.append(user_national_id)
         if (user_login in users):
          while(True):
           u=raw_input('what can we help you at today\n(1)to see vaccination centers and vaccination types\n(2)to reserve vaccination\n(3)for seeing you date\n(4)for exiting\n')
           if(u=='1'):
              vaccination_centers_or_vaccination_types=raw_input('what you want\n(1)to see vaccination centers\n(2)to see vaccination types\n(3)exit\n')
              if(vaccination_centers_or_vaccination_types=='1'):
                print(vecatine_centers)
                continue
              elif(vaccination_centers_or_vaccination_types=='2'):
                print(vaccine_typs)
                continue
              elif(vaccination_centers_or_vaccination_types=='3'):
                continue
              else:
                print('invaled input')
                continue
           elif(u=='2'):
                while(True):
                 user_national_id = raw_input('Please enter your national ID number: ')
                 user_choicse_vcation=raw_input('please enter the id of vcation center you want:')
                 user_choicse_vcation_types=raw_input('please enter the vcation you want:')
                 user_id_regester_found=False
                 for sublist in user_Reserve_vaccination:
                   if user_national_id in sublist:
                     user_id_regester_found=True
                 if(user_id_regester_found):
                   print('you resirevd a date wait for your date to be shdcwel ')
                 else:
                  user_resirv=[]
                  user_resirv.append(user_national_id)
                  user_resirv.append(user_choicse_vcation)
                  user_resirv.append(user_choicse_vcation_types)
                  user_Reserve_vaccination.insert(0,user_resirv)
                  print('you resirevd a date')
                  break
           elif(u=='3'):
             user_date_see=raw_input('please enter your id\n')
             user_date_see_trau=True
             for sublist in user_dates:
               if (user_date_see in sublist):
                 print(sublist)         
                 break
             else:
                 print('you did not reserved a plaes yet or the date is being shdcheid or it declinde')
           elif(u=='4'):
             break
           else:
             print('invalid input')
             continue
         else:
           print('you dont have an acount please regester')
      elif(user_login_or_register=='2'):
             user_name = raw_input('Please enter your name:')
             user_email = raw_input('Please enter your email:')
             user_email_cheek=[]
             user_email_cheek.append(user_email)
             the_at_in=True
             for sublist in user_email_cheek:
               if '@' not in sublist:
                 the_at_in=False
                 break
             if(the_at_in):
               user_password =raw_input('Please enter your password number:')
               user_phone_number = raw_input('Please enter your phone number:') 
               the_phone_number_list=[]
               the_phone_number_list.append(user_phone_number)
               the_phone_number=False
               for sublist in the_phone_number_list:
                if len(sublist)>12 or len(sublist) <12:
                  the_phone_number=True
                  break
               if(the_phone_number):
                 print('invalid phone number')
               else:
                 user_national_id = raw_input('Please enter your NationalId:')
                 the_national_number_cheek=[]
                 the_national_number_cheek.append(user_national_id)
                 the_national_number=False
                 for sublist in the_national_number_cheek:
                  if len(sublist) >14 or len(sublist)<14:
                   the_national_number=True
                   break
                 if(the_national_number):
                   print('invaled national num')
                 else:
                   all_inputs_found = False
                   for sublist in users:
                    if user_email in sublist or user_phone_number in sublist or user_national_id in sublist:
                     all_inputs_found = True
                     print('you have an acount please login')
                     break
                    if(all_inputs_found):
                     print('you have an acount please login')
                     break
                    else:
                     user_input=[]
                     user_input.append(user_name)
                     user_input.append(user_email)
                     user_input.append(user_password)                  
                     user_input.append(user_phone_number)
                     user_input.append(user_national_id)
                     users.insert(0,user_input)
                     print('you have regidterd your acount')
                     print(users)
                     break
             else:
               print('invalid email')   
      else:
        print('invale input')
   else:
      print('wrong input')