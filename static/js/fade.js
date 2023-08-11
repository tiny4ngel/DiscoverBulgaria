document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        let messages = document.querySelectorAll('.messages li');
        messages.forEach(function (message) {
            message.classList.add('fade-out');
            message.addEventListener('animationend', function () {
                message.remove();
            });
        });
    }, 2000);
});

