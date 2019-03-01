require 'discordrb'

bot = Discordrb::Bot.new "appopi@yahoo.com", "e75ySnx6rA9w"

bot.message(with_text: "Ping!") do |event|
  event.respond "Pong!"
end

bot.run