var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');
// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(new logger.transports.Console, {
    colorize: true
});
logger.level = 'debug';
// Initialize Discord Bot
let bot = new Discord.Client({
    token: auth.token,
    autorun: true
});

bot.on('ready', function (evt) {
    logger.info('Connected');
    logger.info('Logged in as: ');
    logger.info(bot.username + ' - (' + bot.id + ')');
});

bot.on('message', function (user, userID, channelID, message, evt) {

    if (message.substring(0, 4) === 'milk') {
        let args = message.substring(5).split(' ');
        let cmd = args[0];

        args = args.splice(1);
        switch(cmd) {

            case 'jmv':
                bot.sendMessage({
                    to: channelID,
                    // send jan michael vincent
                    message: 'Pong!'
                });
                break;
            case 'mint':
                bot.sendMessage({
                    to: channelID,
                    message: 'I crack your butt'
                });
                break;
            case 'trent':
                bot.sendMessage({
                    to: channelID,
                    message: ':boom: KABOOM!'
                });
                break;
        }
    }
});