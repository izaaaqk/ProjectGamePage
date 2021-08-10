const sequelize = require('../config/connection');
const { User } = require('../models');

const userData = require('../src/data.json');

const seedDatabase = async () => {
    await sequelize.sync({ force: true });

    await User.bulkCreate(userData.data);

    process.exit(0);
};

seedDatabase();