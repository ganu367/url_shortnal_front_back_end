# if (db.query(models.User).count() == 0):
# if (request.password == "Pass@1234"):

#     admin_user = models.User(username=request.username, created_by=request.username,
#                              password=hashing.Hash.bcrypt(request.password), is_admin=True)
#     db.add(admin_user)
#     db.commit()
#     db.refresh(admin_user)
#     access_token = tokens.create_access_token(data={"user": {
#         "username": request.username,"isAdmin": True}})

#     return {"access_token": access_token, "token_type": "bearer"}

# else:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail="Incorrect Passwords")

# else:


# delete html code goes below
# <section class="footer">
#       <div class="col footer-about">
#         <a href="" class="brand-lg"> brands<span>U</span>rl </a>
#         <p>
#           BrandURL is a short URL service that offers custom domain branding,
#           password protection, link expiration, and tracking features. BrandURL
#           provides detailed analytics to track clicks, location, and device
#           type.
#         </p>
#       </div>

#       <div class="col footer-company">
#         <h4>Company</h4>
#         <ul>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Teams
#             </a>
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Supports</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer"> FAQ</a>
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer"
#               >Customer Testimonial</a
#             >
#           </li>
#         </ul>
#       </div>
#       <div class="col footer-resources">
#         <h4>Usefull Links</h4>
#         <ul>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Privacy Policy</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Terms & Conditions</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Refunds</a
#             >
#           </li>
#         </ul>
#       </div>
#     </section>

# if not len(request.username) >= 8:
#     raise HTTPException(status_code=status.HTTP_302_FOUND,
#                         detail=f"{request.username} length must be gretter than 8 character.")
# else:
# else:
#     raise HTTPException(status_code=status.HTTP_302_FOUND,
#                         detail=f"{request.username} already exists.")
# if val_user.count() == 0:
#     new_user = models.User(fullname="Shreeganesh", email_address=request.email_address, created_by=request.email_address,
#                             password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     access_token = tokens.create_access_token(data={"user": {
#         "username": request.username, "email_address": request.email_address, "isAdmin": True}})

#     return {"access_token": access_token, "token_type": "bearer"}

# else:


# @router.get('/verifyemail/{verification_code}')
# def VerifyEmail(verification_code: str, db: Session = Depends(get_db)):
#     result = db.query(models.User).filter(
#         models.User.verification_code == verification_code)

#     if not result:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail='Invalid verification code')
#     else:
#         result.update({"is_active": True, "verification_code": None})
#         db.commit()

#     return {"Account verified successfully!"}


######################################JS################################################################################
# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();
#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   // const data = {name:name, mobile_number:mobile, email:email, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify({name:name, email:email, mobile_number:mobile, messages:messages}),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = "Thank You for contact us. Our team will reach you as soon as possible.";
#     console.log(successMessage)
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;
#     console.log(errorMessage)
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);})

#   .then(data => {
#     console.log(data);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });


# async function shortItClick() {
#     const response = await fetch("/api/home/app", {
#       method: "post",
#       headers: {
#         'Content-Type': 'application/json'
#       },
#     //   body: JSON.stringify(data)
#     });
#     if (!response.ok) {
#       throw new Error(`HTTP error! Status: ${response.status}`);
#     }
#     const responseData = await response.json();
#     console.log(responseData)
#     return responseData;
#   }

#  document.addEventListener('DOMContentLoaded', (event) => {
#     document.getElementById("myForm").addEventListener("submit", function (e) {
#        e.preventDefault() // Cancel the default action
#        var catName = document.getElementById('catName').value;
#        fetch('/disable/' + catName, {
#              method: 'POST',
#           })
#           .then(resp => resp.text()) // or, resp.json(), etc.
#           .then(data => {
#              document.getElementById("response").innerHTML = data;
#           })
#           .catch(error => {
#              console.error(error);
#           });
#     });
#  });


# const form = document.getElementById('contact-form');
# const successMessage = document.getElementById('success-message');
# const errorMessage = document.getElementById('error-message');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   // const data = {name:name, mobile_number:mobile, email:email, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify({name:name, email:email, mobile_number:mobile, messages:messages}),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then(data => {
#     console.log(data);
#     if (data.success) {
#       successMessage.style.display = "block";
#       console.log(successMessage)
#     } else {
#       errorMessage.style.display = "block";
#       console.log(errorMessage)
#     }
#     setTimeout(() => {
#       successMessage.style.display = "none";
#       errorMessage.style.display = "none";
#     }, 10000);
#   })

#   .catch(error => {
#     console.error('Error:', error);
#   });

# });


# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   // .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;
#     console.log(successMessage)
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;
#     console.log(errorMessage)
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);})
#   .then(data => {
#     console.log(data);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });

# perfect code
# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#   console.log(data)

#   const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
#   const mobilePattern = /^[0-9]{10}$/;

#   if (!emailPattern.test(email)) {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     document.getElementById('email-input').focus();
#     errorMessage.innerHTML = "Please enter a valid email address.";
#     return;
#   }
#   if (!mobilePattern.test(mobile)){
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     document.getElementById('mobile-input').focus();
#     errorMessage.innerHTML = "Please enter a valid 10-digit mobile number.";
#     return;
#   }


#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-input').value = '';
#     document.getElementById('mobile-input').value = '';
#     document.getElementById('email-input').value = '';
#     document.getElementById('messages-input').value = '';
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;

#      //clear the text fields after successfully submited the form
#      document.getElementById('name-input').value = '';
#      document.getElementById('mobile-input').value = '';
#      document.getElementById('email-input').value = '';
#      document.getElementById('messages-input').value = '';
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);
#   console.log(response);
# })
#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     // console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });


#   const name = document.getElementById('name-fields').value;
#   const mobile = document.getElementById('mobile-fields').value;
#   const email = document.getElementById('email-fields').value;
#   const messages = document.getElementById('messages-fields').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#   console.log(data)

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })

#   .then(response => response.json())

#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-fields').value = '';
#     document.getElementById('mobile-fields').value = '';
#     document.getElementById('email-fields').value = '';
#     document.getElementById('messages-fields').value = '';
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-fields').value = '';
#     document.getElementById('mobile-fields').value = '';
#     document.getElementById('email-fields').value = '';
#     document.getElementById('messages-fields').value = '';
#   }

#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);
#   console.log(response);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# ###########
# const form = document.getElementById('contact-form');
# var successMessage = document.getElementById('success-message');
# var errorMessage = document.getElementById('error-message');

# const name_field = document.getElementById('name-fields');
# const mobile_field = document.getElementById('mobile-fields');
# const email_field = document.getElementById('email-fields');
# const messages_field = document.getElementById('messages-fields');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();
#   if( !validateName()||!validateMobile()||!validateEmail()||!validateMobile()||!validateMassage()){
#     return;
#   }else{
#     const name = document.getElementById('name-fields').value;
#     const mobile = document.getElementById('mobile-fields').value;
#     const email = document.getElementById('email-fields').value;
#     const messages = document.getElementById('messages-fields').value;

#     const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#     console.log(data)

#     fetch('http://127.0.0.1:8000/api/contact-us', {
#       method: 'POST',
#       body: JSON.stringify(data),
#       headers: {
#         'Content-Type': 'application/json'
#       }
#     })
#     .then(response => response.json())
#     .then((response) => {
#       if (response.status === 200){
#       var successMessage = document.getElementById('success-message');
#       successMessage.classList.add("show-message");
#       successMessage.style.display = "block";
#       successMessage.innerHTML = response.detail;

#       //clear the text fields after successfully submited the form
#       document.getElementById('name-fields').value = '';
#       document.getElementById('mobile-fields').value = '';
#       document.getElementById('email-fields').value = '';
#       document.getElementById('messages-fields').value = '';
#     }else {
#       var errorMessage = document.getElementById('error-message');
#       errorMessage.classList.add("show-message");
#       errorMessage.style.display = "block";
#       errorMessage.innerHTML = response.detail;

#        //clear the text fields after successfully submited the form
#       document.getElementById('name-fields').value = '';
#       document.getElementById('mobile-fields').value = '';
#       document.getElementById('email-fields').value = '';
#       document.getElementById('messages-fields').value = '';
#     }
#     setTimeout(() => {
#       var successMessage = document.getElementById('success-message');
#       var errorMessage = document.getElementById('error-message');
#       successMessage.style.display = "none";
#       errorMessage.style.display = "none";
#     }, 5000);
#     console.log(response);
#   })
#     // .catch(error => {
#     //   var errorMessage = document.getElementById('error-message');
#     //   // console.error('Error:', error);
#     //   errorMessage.style.display = "block";
#     //   errorMessage.innerHTML = error.messages;
#     // });
#   }
# });


# function validateName(){
#   const nameValue = name_field.value.trim();
#   if(nameValue === '') {
#       setError('Name field is required');
#       return false;
#     }
#     setError();
#     return true;
# }

# function validateMobile(){
#   const mobileValue = mobile_field.value.trim();
#   if(mobileValue === '') {
#       setError('Mobile number field is required');
#       return false;
#     }else if(!isValidMobileRe(mobileValue)){
#       setError('Mobile number must have 10 didgits');
#       return false;
#     }
#     setError();
#     return true;
# }

# function isValidMobileRe(mobileValue){
#   // const mobileValue = mobile_field.value.trim();
#   const mobilePattern = /^[0-9]{10}$/;
#   return mobilePattern.test(mobileValue);
# }

# function validateEmail(){
#   const emailValue = email_field.value.trim();
#   if(emailValue==='') {
#     setError('Email fields is required');
#     return false;
#     } else if (!isValidEmailPattern(emailValue)) {
#       setError('Provide a valid email address');
#       return false;
#      }
#   setError();
#   return true;
# }

# function isValidEmailPattern(emailValue){
#   // const emailValue = email_field.value.trim();
#   const emailPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
#   return emailPattern.test(String(emailValue).toLowerCase());
# }

# function validateMassage(){
#  const messageValue = messages_field.value.trim();
#  if(messageValue===''){
#   setError('Messages fields is required');
#   return false;
#  }
#  setError()
#  return true;
# }

# const setError = (message) => {
#   errorMessage.classList.add("show-message");
#   errorMessage.style.display = "block";
#   errorMessage.innerText = message;
# }
# const setSuccess = () => {
#   successMessage.classList.add("show-message");
#   successMessage.style.display = "block";
#   successMessage.innerText = "form submitted succesfully";
#   errorMessage.classList.remove('show-message');
# }
