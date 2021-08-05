const faker = require('faker');

const firstName = faker.name.firstName();
const lastName = faker.name.lastName();
const eMail = faker.internet.email();
const avatar = faker.image.avatar();
const password = faker.internet.password();

console.log({firstName,lastName,
 eMail, avatar, password});