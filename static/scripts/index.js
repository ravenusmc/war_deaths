//This function ensures that the user has entered the correct value at the login form.
function validateForm(){
    if (document.forms[0].username.value == "" || document.forms[0].password.value == "" ){
        alert('Please ensure you enter in both a username or password');
        return false;
    }
    return true;
}
