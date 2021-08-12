const express = require('express');
const routes = require('./controllers');
const sequelize = require('./config/connection');
const exphbs  = require('express-handlebars');

const app = express();
const PORT = process.env.PORT || 3001;

const hbs = exphbs.create({ });

app.engine('handlebars', exphbs());
app.set('view engine', 'handlebars');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(routes);

sequelize.sync({ force: false}).then(() => {
    app.listen(PORT, () => console.log (`Now listening on http://localhost:${PORT}`));
});

