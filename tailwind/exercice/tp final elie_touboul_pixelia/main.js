document.querySelector('#theme').addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
});

document.querySelector('#burger').addEventListener('click', () => {
    document.querySelector('#nav-menu').classList.toggle('hidden');
});