// Obtén todas las tarjetas y los botones
const cards = document.querySelectorAll('.card');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
let currentIndex = 0;

// Muestra la primera tarjeta
cards[currentIndex].style.display = 'block';

// Función para mostrar la siguiente tarjeta
function showNextCard() {
    cards[currentIndex].style.display = 'none'; // Oculta la tarjeta actual
    currentIndex = (currentIndex + 1) % cards.length; // Calcula el índice de la siguiente tarjeta
    cards[currentIndex].style.display = 'block'; // Muestra la siguiente tarjeta
}

// Función para mostrar la tarjeta anterior
function showPrevCard() {
    cards[currentIndex].style.display = 'none'; // Oculta la tarjeta actual
    currentIndex = (currentIndex - 1 + cards.length) % cards.length; // Calcula el índice de la tarjeta anterior
    cards[currentIndex].style.display = 'block'; // Muestra la tarjeta anterior
}

// Muestra la siguiente tarjeta cuando se hace clic en el botón "Siguiente"
nextBtn.addEventListener('click', showNextCard);

// Muestra la tarjeta anterior cuando se hace clic en el botón "Anterior"
prevBtn.addEventListener('click', showPrevCard);
