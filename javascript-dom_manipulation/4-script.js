document.getElementById('add_item').onclick = () => {
    const ulElement = document.querySelector('.my_list');
    const newLi = document.createElement('li');
    newLi.textContent = 'Item';
    ulElement.appendChild(newLi);
};
