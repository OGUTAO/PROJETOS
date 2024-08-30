// Função para salvar o contato no localStorage
function saveContact(name, phone) {
    let contacts = JSON.parse(localStorage.getItem('contacts')) || [];
    contacts.push({ name: name, phone: phone });
    localStorage.setItem('contacts', JSON.stringify(contacts));
}

// Função para carregar e exibir os contatos na página "Meus Contatos"
function loadContacts() {
    const contactsTable = document.getElementById('contactsTable');
    const contacts = JSON.parse(localStorage.getItem('contacts')) || [];

    if (contacts.length === 0) {
        const row = contactsTable.insertRow();
        const cell = row.insertCell(0);
        cell.colSpan = 2;
        cell.textContent = 'Nenhum contato salvo ainda.';
        cell.style.textAlign = 'center';
        return;
    }

    contacts.forEach(contact => {
        if (contact.name && contact.phone) {
            const row = contactsTable.insertRow();
            const nameCell = row.insertCell(0);
            const phoneCell = row.insertCell(1);
            nameCell.textContent = contact.name;
            phoneCell.textContent = contact.phone;
        }
    });
}

// Função para carregar os contatos na página principal
function loadRecentContacts() {
    const contactList = document.getElementById('contactList');
    const contacts = JSON.parse(localStorage.getItem('contacts')) || [];

    if (contacts.length === 0) {
        contactList.innerHTML = '<p>Não há contatos recentes ainda. Adicione um novo contato para que ele apareça aqui.</p>';
        return;
    }

    // Exibe apenas os 2 últimos contatos
    const recentContacts = contacts.slice(-2).reverse();

    contactList.innerHTML = recentContacts.map(contact => {
        if (contact.name && contact.phone) {
            return `
                <div class="contact-item">
                    <strong>${contact.name}</strong> - ${contact.phone}
                </div>
            `;
        }
        return '';
    }).join('');
}

// Função para lidar com o envio do formulário de contato
function handleFormSubmit(event) {
    event.preventDefault();
    const name = event.target.elements.nome.value.trim();
    const phone = event.target.elements.telefone.value.trim();

    if (name && phone) {
        saveContact(name, phone);
        window.location.href = 'index.html'; // Redireciona para a página principal após adicionar o contato
    }
}

// Adiciona um ouvinte de evento para o formulário de contato na página de novo contato
document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', handleFormSubmit);
    }

    if (document.getElementById('contactsTable')) {
        loadContacts(); // Carrega os contatos na aba "Meus Contatos"
    }

    if (document.getElementById('contactList')) {
        loadRecentContacts(); // Carrega os contatos recentes na página principal
    }
});
