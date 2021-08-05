const faker = require('faker');
const fs = require('fs');

function generateUsers() {
    let users = [];
    for (let id = 1; id <= 10; id++) {
        const firstName = faker.name.firstName();
        const lastName = faker.name.lastName();
        const eMail = faker.internet.email();
        const avatar = faker.image.avatar();
        const password = faker.internet.password();

        users.push({
            id: id,
            firstName: firstName,
            lastName: lastName,
            email: eMail,
            avatar: avatar,
            password: password
        });
    }
    return { data: users}
}

const generatedData = generateUsers();
fs.writeFileSync('data.json',JSON.stringify(generatedData, null, "\t"));