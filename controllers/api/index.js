const router = require('express').Router();
const { User } = require('../../models');

router.post('/users', async (req, res) => {
    try {
        const newUser = User.create({
            firstName: req.body.firstName,
            lastName: req.body.lastName,
            email: req.body.email,
            password: req.body.password,
            avatar: req.body.avatar,
        });
        if (newUSer) {
            return res.redirect('/');
        }
        res.json(401).json({ message: 'No user was created' });
    } catch (e) {
      res.status(401).josn(e);
    }
})

module.exports = router;
