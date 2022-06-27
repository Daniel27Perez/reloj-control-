$("#formLogin").validate({
  errorClass: "my-error-class",
  validClass: "my-valid-class",
    rules:{
      username: "required",
      password: "required"
    },
    messages: {
      username: "Favor ingresar el nombre de usuario",
      password: "Favor ingresar la contraseña"
    }
  });
  

$("#formRegistro").validate({
   errorClass: "my-error-class",
   validClass: "my-valid-class",
  rules:{
    username: {
      required: true,
      minlength: 10,
      maxlength: 20
      
    },
    email: {
      required: true,
      email: true
    },
    password1: {
      required: true,
      minlength: 10
    },
    password2:  {
      required: true,
      minlength: 10,
      equalTo: "#password1"
    },

    last_name: "required",
    first_name: "required",
    asunto: "required",
    mensaje: "required"
  },
  messages: {
    username: {
      minlength: "Minimo de 10 caracteres",
      maxlength: "Maximo de 20 caracteres"
    },
    password1: {
      minlength: "Minimo de 8 caracteres" 
    },
    password2 :"Repetir contraseña anterior"

  }
});

