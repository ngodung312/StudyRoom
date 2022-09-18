console.log('main.js');

var labelUsername = document.getElementById("label-username");
var usernameInput = document.getElementById("username");
var btnJoin = document.getElementById("join-btn");
console.log(usernameInput)

var username;
btnJoin.addEventListener('click', () => {
    username = usernameInput.value;
    console.log('username:', username);

    if (username == ''){
        return;
    }
    usernameInput.value = '';
    usernameInput.disabled = true;
    usernameInput.style.visibility = 'hidden';
    btnJoin.disabled = true;
    btnJoin.style.visibility = 'hidden';

    var labelUsername = document.getElementById('label-username');
    labelUsername.innerHTML = username;
});