const nameInput = document.querySelector('input[name=spell_name]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {

    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')         // Replace & with 'and'
        .replace(/[\s\W-]+/g, '-')      // Replace spaces, non-word characters and dashes with a single dash (-)

};

nameInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(nameInput.value));
});
