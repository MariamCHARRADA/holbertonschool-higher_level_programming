document.getElementById('toggle_header').onclick = () => {
    const header = document.querySelector('header');
    const classAttr = header.getAttribute('class');

    if (classAttr === 'red') {
        header.setAttribute('class', 'green');
    } else {
        header.setAttribute('class', 'red');
    }
}
