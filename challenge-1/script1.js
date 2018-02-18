function generate_magic_number() {
    return Math.floor(Math.random() * 1000000)
}

function check_guess(){

    the_guess = document.getElementById('guess').value;
    if (the_guess == magic_number){
        alert(atob("dGhlIHNlY3JldCB3b3JkIGlzIEZJUkVGTFk="))
    } else {
        alert("nah! Guess again!")
    }
    
    return false;
}

var magic_number = generate_magic_number();


