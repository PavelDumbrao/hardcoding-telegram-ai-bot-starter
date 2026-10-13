# Обзор 100+ публичных GitHub-источников для Telegram AI Bot Starter

> Дата среза: 13 октября 2026. Это **первичный скрининг карточек репозиториев** (название, описание, язык, категория и релевантность), а **не** полный аудит исходного кода каждого проекта. У финалистов дополнительно прочитаны README; технические решения сверены с первичной документацией.

## Зачем и как отбирали

- Цель: один минимальный учебный шаблон, запускаемый локально без VPS, Docker и базы данных-сервера.
- Сначала отфильтровали GitHub по aiogram/Python, Telegram chatbot/OpenAI и starter/template (архивы исключены там, где это поддерживалось запросом).
- Сравнили кандидатов по сложности первого запуска, наличию LLM-подключения, понятности структуры, русскому учебному сценарию и потенциалу для расширения.
- Ниже — отдельные реально полученные репозитории, без повторов между категориями.
- В глубину изучены README: BaggerFast/AiogramTemplate, arturboyun/AiogramBotTemplate, welel/aiogram-bot-template, father-bot/chatgpt_telegram_bot, kaxing/simple-telegram-gpt-bot и nalgeon/pokitoki. Также сверены текущий собственный шаблон и его файлы.

## Почему выбран свой существующий шаблон

**PavelDumbrao/hardcoding-telegram-ai-bot-starter** — уже публичный; содержит aiogram 3, простые router-обработчики, SQLite, OpenAI-compatible `/chat/completions`, /start, /help, /reset, `.env.example`, тесты, CI и русскоязычный промпт для кодинг-агента. Не нужно создавать конкурирующую копию.

### Сравнение читаемых финалистов

| Репозиторий | Плюс | Почему не основа первого урока |
|---|---|---|
| BaggerFast/AiogramTemplate | Классическая структура handlers и базы | Нет учебной AI-интеграции из коробки |
| arturboyun/AiogramBotTemplate | Подходит для production архитектуры | FastAPI, Redis, PostgreSQL и миграции усложняют старт |
| welel/aiogram-bot-template | Чистый базовый aiogram 3 | Нужно отдельно собирать AI и память |
| father-bot/chatgpt_telegram_bot | Много готовых AI-функций | Слишком много режимов для первого занятия |
| kaxing/simple-telegram-gpt-bot | Простая AI-концепция | Меньше учебной структуры для поэтапного расширения |
| nalgeon/pokitoki | OpenAI-compatible, чат/группы | Настройка множества режимов отвлекает от первого результата |

## Официальные технические источники

- [Telegram: BotFather и токен](https://core.telegram.org/bots/tutorial)
- [Telegram: Bot API](https://core.telegram.org/bots/api)
- [Telegram: Bots FAQ / updates](https://core.telegram.org/bots/faq)
- [aiogram 3: Dispatcher и polling](https://docs.aiogram.dev/en/dev-3.x/dispatcher/dispatcher.html)
- [aiogram 3: миграция с 2.x](https://docs.aiogram.dev/en/dev-3.x/migration_2_to_3.html)
- [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
- [Python venv](https://docs.python.org/3/library/venv.html)

## Реестр просмотренных карточек GitHub

Всего уникальных кандидатных репозиториев в данном срезе: **145**.

1. [aiogram/aiogram](https://github.com/aiogram/aiogram) — aiogram
2. [ilyarolf/AiogramShopBot](https://github.com/ilyarolf/AiogramShopBot) — aiogram
3. [BEDOLAGA-DEV/remnawave-bedolaga-telegram-bot](https://github.com/BEDOLAGA-DEV/remnawave-bedolaga-telegram-bot) — aiogram
4. [Tishka17/aiogram_dialog](https://github.com/Tishka17/aiogram_dialog) — aiogram
5. [noXplode/aiogram_calendar](https://github.com/noXplode/aiogram_calendar) — aiogram
6. [BaggerFast/AiogramTemplate](https://github.com/BaggerFast/AiogramTemplate) — aiogram
7. [PythonHubStudio/aiogram-3-course-telegram-bot](https://github.com/PythonHubStudio/aiogram-3-course-telegram-bot) — aiogram
8. [rlxrd/aiogram_sqla_sample](https://github.com/rlxrd/aiogram_sqla_sample) — aiogram
9. [MasterGroosha/telegram-feedback-bot](https://github.com/MasterGroosha/telegram-feedback-bot) — aiogram
10. [jonowo/on9wordchainbot](https://github.com/jonowo/on9wordchainbot) — aiogram
11. [serg-akulov/turner-telegram-bot](https://github.com/serg-akulov/turner-telegram-bot) — aiogram
12. [arturboyun/AiogramBotTemplate](https://github.com/arturboyun/AiogramBotTemplate) — aiogram
13. [DaniilDonskoy/Shop-bot](https://github.com/DaniilDonskoy/Shop-bot) — aiogram
14. [OldCodersClub/LariskaBot](https://github.com/OldCodersClub/LariskaBot) — aiogram
15. [nessshon/support-bot](https://github.com/nessshon/support-bot) — aiogram
16. [Fsoky/anonimchatbot-aiogram3](https://github.com/Fsoky/anonimchatbot-aiogram3) — aiogram
17. [MasterGroosha/telegram-report-bot](https://github.com/MasterGroosha/telegram-report-bot) — aiogram
18. [anvarnarz/aiogram-bot-shablon](https://github.com/anvarnarz/aiogram-bot-shablon) — aiogram
19. [donbarbos/telegram-bot-template](https://github.com/donbarbos/telegram-bot-template) — aiogram
20. [welel/dialog-chat-bot](https://github.com/welel/dialog-chat-bot) — aiogram
21. [netbriler/aiogram-peewee-template](https://github.com/netbriler/aiogram-peewee-template) — aiogram
22. [MassonNN/masson-aiogram-template](https://github.com/MassonNN/masson-aiogram-template) — aiogram
23. [innightwolfsleep/llm_telegram_bot](https://github.com/innightwolfsleep/llm_telegram_bot) — aiogram
24. [mamashin/tg-bot-fastapi-aiogram](https://github.com/mamashin/tg-bot-fastapi-aiogram) — aiogram
25. [soldatov-ss/flibusta-telegram-bot](https://github.com/soldatov-ss/flibusta-telegram-bot) — aiogram
26. [erfjab/holderbot](https://github.com/erfjab/holderbot) — aiogram
27. [welel/aiogram-bot-template](https://github.com/welel/aiogram-bot-template) — aiogram
28. [Brondee/Telegram-shop-bot](https://github.com/Brondee/Telegram-shop-bot) — aiogram
29. [Priler/telegramStarsBot](https://github.com/Priler/telegramStarsBot) — aiogram
30. [Mak5er/Downloader-Bot](https://github.com/Mak5er/Downloader-Bot) — aiogram
31. [Gunthersuper/aiogram-lessons](https://github.com/Gunthersuper/aiogram-lessons) — aiogram
32. [MasterGroosha/telegram-bombsweeper-bot](https://github.com/MasterGroosha/telegram-bombsweeper-bot) — aiogram
33. [bomzheg/KarmaBot](https://github.com/bomzheg/KarmaBot) — aiogram
34. [rodion-gudz/telegram-bot-template](https://github.com/rodion-gudz/telegram-bot-template) — aiogram
35. [bekmuxtorov/midjourney-telegram-bot](https://github.com/bekmuxtorov/midjourney-telegram-bot) — aiogram
36. [BotYanis/Casino_bot](https://github.com/BotYanis/Casino_bot) — aiogram
37. [andrew000/aiogram-template](https://github.com/andrew000/aiogram-template) — aiogram
38. [nessshon/aiogram-tonconnect](https://github.com/nessshon/aiogram-tonconnect) — aiogram
39. [BaggerFast/AdvancedUserTelegramBot](https://github.com/BaggerFast/AdvancedUserTelegramBot) — aiogram
40. [codemurt/aiogram-fastapi-webhook-render-template](https://github.com/codemurt/aiogram-fastapi-webhook-render-template) — aiogram
41. [omadli/Django-Webhook-Aiogram](https://github.com/omadli/Django-Webhook-Aiogram) — aiogram
42. [exmanka/ksiVPN-telegram-bot](https://github.com/exmanka/ksiVPN-telegram-bot) — aiogram
43. [realkarych/aioplate](https://github.com/realkarych/aioplate) — aiogram
44. [UznetDev/Aiogram-Bot-Template](https://github.com/UznetDev/Aiogram-Bot-Template) — aiogram
45. [Priler/tgbotbase](https://github.com/Priler/tgbotbase) — aiogram
46. [bralbral/telegram-feedback-bot](https://github.com/bralbral/telegram-feedback-bot) — aiogram
47. [TimNekk/copier-telegram-bot](https://github.com/TimNekk/copier-telegram-bot) — aiogram
48. [olkhovichs/groceryShop_TelegramBot](https://github.com/olkhovichs/groceryShop_TelegramBot) — aiogram
49. [rashidovich2/TelegramGoodsInbot](https://github.com/rashidovich2/TelegramGoodsInbot) — aiogram
50. [dimaplel/telegram-suggestions-bot](https://github.com/dimaplel/telegram-suggestions-bot) — aiogram
51. [MrConsoleka/aiogram-miniapp-template](https://github.com/MrConsoleka/aiogram-miniapp-template) — aiogram
52. [sobirjonovme/FontChanger_bot](https://github.com/sobirjonovme/FontChanger_bot) — aiogram
53. [pylounge/fdcbaza-telegram-bot](https://github.com/pylounge/fdcbaza-telegram-bot) — aiogram
54. [amirho3inf/aiogram-structured](https://github.com/amirho3inf/aiogram-structured) — aiogram
55. [TegroTON/SMMPanel-SMOService-Telegram-Bot](https://github.com/TegroTON/SMMPanel-SMOService-Telegram-Bot) — aiogram
56. [undrcrxwn/hide-this-bot](https://github.com/undrcrxwn/hide-this-bot) — aiogram
57. [Th3Kanashii/telegram-virtual-casino-bot](https://github.com/Th3Kanashii/telegram-virtual-casino-bot) — aiogram
58. [lleballex/magiceden-bot](https://github.com/lleballex/magiceden-bot) — aiogram
59. [vladislav-bordiug/ChatGPT_DALL_E_StableDiffusion_Telegram_Bot](https://github.com/vladislav-bordiug/ChatGPT_DALL_E_StableDiffusion_Telegram_Bot) — aiogram
60. [krystlepalace/characterai-telegram-bot](https://github.com/krystlepalace/characterai-telegram-bot) — aiogram
61. [kmsint/aiogram_course_bot_template](https://github.com/kmsint/aiogram_course_bot_template) — aiogram
62. [nessshon/token-access-control-bot](https://github.com/nessshon/token-access-control-bot) — aiogram
63. [czbag/aiogram-bot-template](https://github.com/czbag/aiogram-bot-template) — aiogram
64. [twers1/telegram-bot-shop](https://github.com/twers1/telegram-bot-shop) — aiogram
65. [Birdi7/Template-Telegram-bot](https://github.com/Birdi7/Template-Telegram-bot) — aiogram
66. [zerox9dev/Vidzilla](https://github.com/zerox9dev/Vidzilla) — aiogram
67. [o-murphy/aiogram3_calendar](https://github.com/o-murphy/aiogram3_calendar) — aiogram
68. [TrackLine/telegram-shop-bot](https://github.com/TrackLine/telegram-shop-bot) — aiogram
69. [Birdi7/inline-timepicker](https://github.com/Birdi7/inline-timepicker) — aiogram
70. [itzddos/ecommerce-telegram-bot](https://github.com/itzddos/ecommerce-telegram-bot) — aiogram
71. [schmdtt/alice-telegram-bot](https://github.com/schmdtt/alice-telegram-bot) — aiogram
72. [GamePad64/python-telegram-bot-django-persistence](https://github.com/GamePad64/python-telegram-bot-django-persistence) — aiogram
73. [tochilkinva/tg_bot_stt_tts](https://github.com/tochilkinva/tg_bot_stt_tts) — aiogram
74. [maratx86/aiogram-timepicker](https://github.com/maratx86/aiogram-timepicker) — aiogram
75. [sobirjonovme/WhisperBot](https://github.com/sobirjonovme/WhisperBot) — aiogram
76. [rlxrd/aiogrambot](https://github.com/rlxrd/aiogrambot) — aiogram
77. [galinaalperovich/chatgpt-api-tg-bot](https://github.com/galinaalperovich/chatgpt-api-tg-bot) — aiogram
78. [Hamster-Prime/Smart_Group_Bot](https://github.com/Hamster-Prime/Smart_Group_Bot) — aiogram
79. [mangunan/smshub_aiogram_light](https://github.com/mangunan/smshub_aiogram_light) — aiogram
80. [evgfilim1/spin_everyday_bot](https://github.com/evgfilim1/spin_everyday_bot) — aiogram
81. [EverythingSuckz/aiogram-serverless-bot](https://github.com/EverythingSuckz/aiogram-serverless-bot) — aiogram
82. [veenrokdalv/aiogram-telegram-bot-template](https://github.com/veenrokdalv/aiogram-telegram-bot-template) — aiogram
83. [BigDaddyAman/telegram-file-to-link-bot](https://github.com/BigDaddyAman/telegram-file-to-link-bot) — aiogram
84. [Priler/tgbotbase3](https://github.com/Priler/tgbotbase3) — aiogram
85. [AndrewKentavr/ScipIO](https://github.com/AndrewKentavr/ScipIO) — aiogram
86. [father-bot/chatgpt_telegram_bot](https://github.com/father-bot/chatgpt_telegram_bot) — AI/chatbot
87. [xluxeq/GPT3-Telegram-Chatbot](https://github.com/xluxeq/GPT3-Telegram-Chatbot) — AI/chatbot
88. [nalgeon/pokitoki](https://github.com/nalgeon/pokitoki) — AI/chatbot
89. [wxc971231/TelegramChatBot](https://github.com/wxc971231/TelegramChatBot) — AI/chatbot
90. [Deemocean/GhostGPT](https://github.com/Deemocean/GhostGPT) — AI/chatbot
91. [kaxing/simple-telegram-gpt-bot](https://github.com/kaxing/simple-telegram-gpt-bot) — AI/chatbot
92. [almienava/telegrambot-openai](https://github.com/almienava/telegrambot-openai) — AI/chatbot
93. [shamspias/langchain-telegram-gpt-chatbot](https://github.com/shamspias/langchain-telegram-gpt-chatbot) — AI/chatbot
94. [iamsushanth/telegram-chatbot-using-open-ai-python-heroku](https://github.com/iamsushanth/telegram-chatbot-using-open-ai-python-heroku) — AI/chatbot
95. [emingenc/telegramGPT](https://github.com/emingenc/telegramGPT) — AI/chatbot
96. [FlyingFathead/TelegramBot-OpenAI-API](https://github.com/FlyingFathead/TelegramBot-OpenAI-API) — AI/chatbot
97. [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) — AI/chatbot
98. [paulpierre/RasaGPT](https://github.com/paulpierre/RasaGPT) — AI/chatbot
99. [stevenyu113228/OpenAI-GPT-3-Telegram-Chatbot](https://github.com/stevenyu113228/OpenAI-GPT-3-Telegram-Chatbot) — AI/chatbot
100. [thewickedkarma/Amadeus](https://github.com/thewickedkarma/Amadeus) — AI/chatbot
101. [KroMiose/nekro-agent](https://github.com/KroMiose/nekro-agent) — AI/chatbot
102. [Raiseku/Telegram-ChatGPT-bot](https://github.com/Raiseku/Telegram-ChatGPT-bot) — AI/chatbot
103. [yesbhautik/Master-AI-BOT](https://github.com/yesbhautik/Master-AI-BOT) — AI/chatbot
104. [torrresagus/openAI-woocommerce-chatbot-telegram](https://github.com/torrresagus/openAI-woocommerce-chatbot-telegram) — AI/chatbot
105. [dhir4j/chatgpt-bot-telegram](https://github.com/dhir4j/chatgpt-bot-telegram) — AI/chatbot
106. [S1M0N38/telegram-GPT](https://github.com/S1M0N38/telegram-GPT) — AI/chatbot
107. [FlamingoFiesta/Chatgpt-Claude_telegram_bot_with_payment_system](https://github.com/FlamingoFiesta/Chatgpt-Claude_telegram_bot_with_payment_system) — AI/chatbot
108. [s-nagaev/chibi](https://github.com/s-nagaev/chibi) — AI/chatbot
109. [kravchik/orc](https://github.com/kravchik/orc) — AI/chatbot
110. [Flagro/TelegramRPBot](https://github.com/Flagro/TelegramRPBot) — AI/chatbot
111. [Leoksu/DewChatGPT](https://github.com/Leoksu/DewChatGPT) — AI/chatbot
112. [vkopitsa/terminal-assistant-chat](https://github.com/vkopitsa/terminal-assistant-chat) — AI/chatbot
113. [decentboyy/ChatGpt_TG](https://github.com/decentboyy/ChatGpt_TG) — AI/chatbot
114. [andryplekhanov/django-aiogram-template](https://github.com/andryplekhanov/django-aiogram-template) — templates
115. [MrConsoleka/aiogram-bot-template](https://github.com/MrConsoleka/aiogram-bot-template) — templates
116. [BushlanovDev/aiogram-fastapi-bot-template](https://github.com/BushlanovDev/aiogram-fastapi-bot-template) — templates
117. [irakhimianov/aiogram_bot_template](https://github.com/irakhimianov/aiogram_bot_template) — templates
118. [Taqiy-M/aiogram-template](https://github.com/Taqiy-M/aiogram-template) — templates
119. [TimNekk/TGBotTemplate](https://github.com/TimNekk/TGBotTemplate) — templates
120. [BLazzeD21/py-aiogram-template-bot](https://github.com/BLazzeD21/py-aiogram-template-bot) — templates
121. [soxibjonovich/telegram_bot_template](https://github.com/soxibjonovich/telegram_bot_template) — templates
122. [MuhammadislomMuhammadaliyev/aiogram-bot-template](https://github.com/MuhammadislomMuhammadaliyev/aiogram-bot-template) — templates
123. [nessshon/aiogram-starlette-template](https://github.com/nessshon/aiogram-starlette-template) — templates
124. [onlysharifjon/Telegram-bot-Template-Aiogram](https://github.com/onlysharifjon/Telegram-bot-Template-Aiogram) — templates
125. [nichind/Aiogram3-Telegram-Bot-Template](https://github.com/nichind/Aiogram3-Telegram-Bot-Template) — templates
126. [AlexanderKorataev/aiogram-bot-template](https://github.com/AlexanderKorataev/aiogram-bot-template) — templates
127. [hexfrost/fastapi-aiogram-template](https://github.com/hexfrost/fastapi-aiogram-template) — templates
128. [vitaliipanasiuk/TelegramBot-template](https://github.com/vitaliipanasiuk/TelegramBot-template) — templates
129. [nazar220160/AiogramTemplate](https://github.com/nazar220160/AiogramTemplate) — templates
130. [djimboy/djimbo_template_aio3](https://github.com/djimboy/djimbo_template_aio3) — templates
131. [bnutfilloyev/TGbot-template](https://github.com/bnutfilloyev/TGbot-template) — templates
132. [ruslan-korneev/telegram-bot-postgres-docker-template](https://github.com/ruslan-korneev/telegram-bot-postgres-docker-template) — templates
133. [corruptmane/aiogram_template](https://github.com/corruptmane/aiogram_template) — templates
134. [Lems0n/aiogram_template](https://github.com/Lems0n/aiogram_template) — templates
135. [PetruninKV/base_structure_telegrambot](https://github.com/PetruninKV/base_structure_telegrambot) — templates
136. [FajoX1/tgbotbase-aiogram3](https://github.com/FajoX1/tgbotbase-aiogram3) — templates
137. [niko0701/aiogram-bot-template](https://github.com/niko0701/aiogram-bot-template) — templates
138. [lleballex/aiogram-template](https://github.com/lleballex/aiogram-template) — templates
139. [mlt-melt/aiogram3BotTemplate](https://github.com/mlt-melt/aiogram3BotTemplate) — templates
140. [Wiped-Out/telegram-bot-template](https://github.com/Wiped-Out/telegram-bot-template) — templates
141. [aoulaa/aiogram-lambda-template](https://github.com/aoulaa/aiogram-lambda-template) — templates
142. [astronuttt/aiogram-template](https://github.com/astronuttt/aiogram-template) — templates
143. [Er1one/telegram-bot-template](https://github.com/Er1one/telegram-bot-template) — templates
144. [NotBupyc/aiogram-bot-template](https://github.com/NotBupyc/aiogram-bot-template) — templates
145. [Serg-one/aiogram-bot](https://github.com/Serg-one/aiogram-bot) — templates

## Важное ограничение исследования

100+ просмотренных GitHub-карточек не означают, что у всех 100+ проведены аудит безопасности, проверка лицензии или запуск тестов. Для копирования чужого кода нужны отдельная лицензионная и техническая проверки. В учебный проект переносится **не код сторонних репозиториев**, а обобщённые архитектурные выводы.
