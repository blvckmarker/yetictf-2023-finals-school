from typing import NamedTuple
import requests, enum, typing, random, string, json
import secrets
import os


agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/62.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 Maxthon/5.3.8.2000',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
]

def rnd_agent():
    return random.choice(agents)

PORT = 2222
names = ('Aaberg', 'Abbot', 'Abernon', 'Abram', 'Ackerley', 'Adalbert', 'Adamsen', 'Ade', 'Ader', 'Adlare', 'Adore', 'Adrienne', 'Afton', 'Agle', 'Ahab', 'Aida', 'Ailyn', 'Ajay', 'Alabaster', 'Alarise', 'Albertine', 'Alcott', 'Aldric', 'Alejoa', 'Alexandr', 'Alfons', 'Alice', 'Alisia', 'Allare', 'Allina', 'Allys', 'Aloise', 'Alrich', 'Alva', 'Alwin', 'Amadas', 'Amand', 'Amasa', 'Ambrosia', 'Amethist', 'Ammann', 'Ana', 'Anastice', 'Anderegg', 'Andres', 'Anet', 'Angelita', 'Anissa', 'Annabelle', 'Annie', 'Anselmo', 'Antone', 'Anzovin', 'Aprilette', 'Arbe', 'Ardehs', 'Ardrey', 'Argyle', 'Arielle', 'Arleyne', 'Armando', 'Arnelle', 'Arratoon', 'Artima', 'Arvonio', 'Asher', 'Ashraf', 'Astraea', 'Athal', 'Atrice', 'Auberon', 'Audra', 'Augusta', 'Aurelius', 'Autry', 'Avictor', 'Axe', 'Aziza', 'Bachman', 'Baiel', 'Bakki', 'Ballard', 'Bander', 'Bar', 'Barbi', 'Barimah', 'Barnie', 'Barry', 'Bartley', 'Bashuk', 'Batha', 'Baudoin', 'Bayly', 'Beasley', 'Beberg', 'Beeck', 'Behrens', 'Belayneh', 'Belle', 'Bendicta', 'Benil', 'Bennink', 'Berardo', 'Bergmann', 'Berlauda', 'Bernelle', 'Berry', 'Bertolde', 'Bethel', 'Betty', 'Bevis', 'Bible', 'Bigod', 'Bilow', 'Birdie', 'Bixby', 'Blakelee', 'Blaseio', 'Blithe', 'Bluhm', 'Bobbette', 'Boehmer', 'Bohman', 'Bollen', 'Bonina', 'Booker', 'Borden', 'Borreri', 'Boucher', 'Bowden', 'Boycie', 'Brackett', 'Braeunig', 'Brandie', 'Braunstein', 'Breen', 'Brenna', 'Briana', 'Brietta', 'Bringhurst', 'Brittany', 'Broder', 'Bronnie', 'Brott', 'Brunella', 'Bryner', 'Buckley', 'Buffy', 'Bum', 'Burchett', 'Burkley', 'Burny', 'Busby', 'Butte', 'Byrom', 'Cadmarr', 'Caitrin', 'Calia', 'Calloway', 'Camel', 'Campbell', 'Candyce', 'Caplan', 'Carbone', 'Cargian', 'Carlen', 'Carlstrom', 'Carmencita', 'Carolina', 'Carrick', 'Cary', 'Casimire', 'Cassondra', 'Catha', 'Catima', 'Cavanagh', 'Ceciley', 'Celestyn', 'Centonze', 'Chace', 'Chak', 'Chandless', 'Chapman', 'Charla', 'Charmion', 'Chavaree', 'Chema', 'Cherice', 'Chesney', 'Chickie', 'Chiou', 'Chon', 'Christalle', 'Christis', 'Chu', 'Ciapha', 'Cinda', 'Cirone', 'Clarabelle', 'Clarisse', 'Claudio', 'Clein', 'Cleodal', 'Cliff', 'Close', 'Cnut', 'Codee', 'Cohe', 'Colburn', 'Collen', 'Colpin', 'Combe', 'Conchita', 'Conner', 'Constant', 'Cooley', 'Corabelle', 'Cordie', 'Corin', 'Cornelie', 'Corrinne', 'Cosetta', 'Cottrell', 'Covell', 'Craggy', 'Crean', 'Cressler', 'Cristian', 'Crompton', 'Cruickshank', 'Culliton', 'Currey', 'Cutlip', 'Cynara', 'Cyril', 'Dael', 'Dahlstrom', 'Dallis', 'Dambro', 'Danczyk', 'Daniell', 'Dante', 'Darby', 'Darice', 'Darrelle', 'Dasha', 'Davey', 'Dawn', 'Dearborn', 'Decato', 'Deedee', 'Dela', 'Delija', 'Delos', 'Deming', 'Denie', 'Denver', 'Dermot', 'Des', 'Deste', 'Devland', 'Dewitt', 'Dianemarie', 'Dich', 'Dielle', 'Dimitri', 'Dinsmore', 'Dittman', 'Docile', 'Doi', 'Dolphin', 'Dominus', 'Donela', 'Donny', 'Dorcus', 'Dorinda', 'Dorothi', 'Dosi', 'Douglas', 'Downs', 'Dream', 'Driskill', 'Drummond', 'Dudden', 'Dulcia', 'Dunham', 'Durant', 'Durward', 'Duvall', 'Dyanne', 'Eachelle', 'Earley', 'Ebby', 'Eckart', 'Edea', 'Edina', 'Edmonds', 'Edva', 'Egarton', 'Ehrlich', 'Eisenstark', 'Elberta', 'Eldreeda', 'Eleph', 'Eliathan', 'Elish', 'Ellerd', 'Ellora', 'Elnore', 'Elsie', 'Elvis', 'Emalia', 'Emersen', 'Emmalee', 'Emmuela', 'Eng', 'Ennis', 'Ephrayim', 'Erastus', 'Erica', 'Erland', 'Ermine', 'Erroll', 'Esma', 'Estell', 'Ethan', 'Etoile', 'Eugene', 'Euphemie', 'Evander', 'Evelyn', 'Evslin', 'Ezana', 'Fabio', 'Fadil', 'Fairman', 'Fanchon', 'Fari', 'Farny', 'Fasano', 'Faus', 'Fawnia', 'Fedak', 'Feldt', 'Feliza', 'Fenner', 'Feriga', 'Ferrel', 'Fia', 'Fiertz', 'Fillander', 'Fini', 'Firman', 'Fitzpatrick', 'Fleeman', 'Flip', 'Florin', 'Flss', 'Fonsie', 'Forras', 'Foskett', 'France', 'Francoise', 'Franz', 'Freda', 'Fredette', 'French', 'Friedberg', 'Frodeen', 'Fruma', 'Fullerton', 'Fusco', 'Gabrielle', 'Gahan', 'Galatia', 'Gamali', 'Garaway', 'Gare', 'Garlen', 'Garris', 'Gaspar', 'Gauldin', 'Gavrielle', 'Gayner', 'Gefen', 'Gemina', 'Genisia', 'Geoffry', 'Georglana', 'Gerfen', 'Germana', 'Gerstner', 'Gherardi', 'Gibb', 'Giesser', 'Gilberto', 'Gill', 'Gilmore', 'Ginny', 'Girardi', 'Giuditta', 'Gladis', 'Glenda', 'Glover', 'Godber', 'Goer', 'Goldin', 'Gomar', 'Goodden', 'Gordie', 'Gotcher', 'Gow', 'Graham', 'Granny', 'Graybill', 'Greenstein', 'Gregory', 'Greyso', 'Grimbald', 'Groark', 'Grosvenor', 'Gualterio', 'Guild', 'Gunilla', 'Gusba', 'Guthrey', 'Gwenora', 'Hachmann', 'Haerle', 'Haile', 'Haldane', 'Hall', 'Halpern', 'Hamid', 'Hamrnand', 'Hankins', 'Hanser', 'Hardan', 'Harim', 'Harms', 'Harriette', 'Hartmunn', 'Hasheem', 'Hatfield', 'Havener', 'Hayman', 'Hazen', 'Hebert', 'Hedvah', 'Heidie', 'Heise', 'Helenka', 'Helsie', 'Hendry', 'Henricks', 'Hepsiba', 'Hermann', 'Herrah', 'Hertz', 'Hess', 'Hewie', 'Hidie', 'Hilary', 'Hillegass', 'Hime', 'Hiroshi', 'Hoashis', 'Hoem', 'Hola', 'Hollinger', 'Holtorf', 'Honora', 'Horacio', 'Hortense', 'Hound', 'Howlond', 'Huberman', 'Hufnagel', 'Hulen', 'Hun', 'Hurless', 'Hutchinson', 'Hyde', 'Iaria', 'Idel', 'Ieso', 'Ihab', 'Ilise', 'Imelda', 'Infeld', 'Ingold', 'Iny', 'Iphigeniah', 'Irmina', 'Isac', 'Isidora', 'Israel', 'Ive', 'Iz', 'Jacie', 'Jacoba', 'Jacquette', 'Jaffe', 'Jala', 'Jamison', 'Janelle', 'Janis', 'Janyte', 'Jariah', 'Jarvis', 'Jaye', 'Jeanna', 'Jeffcott', 'Jehovah', 'Jen', 'Jennee', 'Jerad', 'Jerol', 'Jesher', 'Jeth', 'Jillana', 'JoAnne', 'Jobe', 'Jody', 'Johanan', 'Johns', 'Jolenta', 'Jones', 'Jordon', 'Joselow', 'Josselyn', 'Jozef', 'Judus', 'Julie', 'Juni', 'Justine', 'Kaela', 'Kaitlynn', 'Kalin', 'Kama', 'Kania', 'Karas', 'Karissa', 'Karlyn', 'Kary', 'Kassity', 'Katheryn', 'Katonah', 'Kaufmann', 'Kaz', 'Keeler', 'Keiko', 'Kelila', 'Kelsy', 'Kendrah', 'Kenneth', 'Kenwee', 'Kerman', 'Kery', 'Kevin', 'Khichabia', 'Kieran', 'Killian', 'Kimmel', 'Kingston', 'Kira', 'Kirsteni', 'Kitty', 'Klement', 'Klos', 'Knowle', 'Kobylak', 'Kolk', 'Konstantine', 'Korenblat', 'Kosel', 'Kowtko', 'Krause', 'Krenn', 'Kristel', 'Krock', 'Krystalle', 'Kumler', 'Kusin', 'Kyla', 'LaMee', 'Lachman', 'Lahey', 'Lali', 'Lammond', 'Lancelot', 'Landry', 'Langston', 'Laraine', 'Larkin', 'Lashondra', 'Latimer', 'Latt', 'Launcelot', 'Lauretta', 'Lavena', 'Lawson', 'LeMay', 'Leanora', 'Leclair', 'Leesen', 'Leid', 'Lela', 'Lemon', 'Lenno', 'Leon', 'Leontina', 'Leshia', 'Letizia', 'Leveridge', 'Lewellen', 'Lezlie', 'Libby', 'Lidia', 'Lila', 'Lily', 'Lindbom', 'Lindy', 'Linnie', 'Lipscomb', 'Liss', 'Liu', 'Lizzy', 'Lodmilla', 'Lolande', 'Longan', 'Lopes', 'Lorena', 'Lorinda', 'Lorry', 'Lotus', 'Loux', 'Lowney', 'Lubeck', 'Lucic', 'Lucy', 'Luelle', 'Lulita', 'Lunneta', 'Lustick', 'Lyford', 'Lynelle', 'Lysander', 'MacGregor', 'Maccarone', 'Macy', 'Madelaine', 'Madonia', 'Magda', 'Magna', 'Mahon', 'Maire', 'Malamud', 'Malia', 'Mallis', 'Malvie', 'Mandi', 'Manny', 'Manya', 'Marcellina', 'Marcoux', 'Margalo', 'Margit', 'Mariano', 'Marigolde', 'Marion', 'Market', 'Marler', 'Maro', 'Marrissa', 'Martelli', 'Martinson', 'Marya', 'Marysa', 'Mastic', 'Mathian', 'Matthaus', 'Maud', 'Maurili', 'Maxentia', 'Mayce', 'Mazonson', 'McClelland', 'McCullough', 'McGraw', 'McKinney', 'McNeely', 'Meaghan', 'Medora', 'Meghan', 'Mela', 'Melessa', 'Mella', 'Melody', 'Mendelsohn', 'Meraree', 'Meredi', 'Merlin', 'Merrill', 'Meta', 'Micaela', 'Michelina', 'Middendorf', 'Mikael', 'Milburr', 'Millar', 'Milon', 'Miner', 'Minta', 'Mirilla', 'Mitinger', 'Modeste', 'Mohr', 'Molly', 'Monika', 'Monteith', 'Mord', 'Morganne', 'Morra', 'Mosa', 'Mossman', 'Moyna', 'Mulcahy', 'Munford', 'Murdock', 'Muslim', 'Myra', 'Naamana', 'Nadean', 'Nahshu', 'Names', 'Nanny', 'Nari', 'Natal', 'Nathanial', 'Nazar', 'Neddy', 'Neile', 'Nellir', 'Neri', 'Nessie', 'Neumark', 'Newby', 'Niall', 'Nicki', 'Nicolella', 'Nightingale', 'Nikos', 'Niobe', 'Noach', 'Noell', 'Nollie', 'Nord', 'Normi', 'Norvell', 'Nozicka', 'Nyhagen', 'Obau', 'Obrien', 'Odele', 'Odom', 'Ogg', 'Olatha', 'Olga', 'Olly', 'Olympe', 'Ondine', 'Oona', 'Orbadiah', 'Orgell', 'Orlando', 'Ornstead', 'Orthman', 'Osborn', 'Ossie', 'Othelia', 'Otto', 'Ozzie', "O'Meara", 'Packer', 'Paige', 'Palma', 'Panayiotis', 'Paola', 'Pardoes', 'Parrish', 'Pascale', 'Patience', 'Patterman', 'Paulita', 'Paxton', 'Pearlman', 'Pedroza', 'Pelaga', 'Pena', 'Pentha', 'Per', 'Perloff', 'Perseus', 'Peterson', 'Petronilla', 'Pfeifer', 'Phene', 'Philine', 'Phillis', 'Phox', 'Piefer', 'Pike', 'Pinter', 'Piselli', 'Plante', 'Plumbo', 'Polito', 'Pomona', 'Popelka', 'Portwine', 'Power', 'Prendergast', 'Priebe', 'Prissie', 'Proudfoot', 'Pryor', 'Pulcheria', 'Puto', 'Queenie', 'Quince', 'Quiteris', 'Rachel', 'Radloff', 'Raffaello', 'Rahr', 'Rakia', 'Ramey', 'Randal', 'Ranit', 'Rapp', 'Ratib', 'Ray', 'Rayshell', 'Rebbecca', 'Redfield', 'Reeva', 'Reiche', 'Reinhard', 'Rem', 'Rene', 'Renwick', 'Reuven', 'Rhea', 'Rhodie', 'Ribble', 'Richela', 'Ricker', 'Riegel', 'Riki', 'Rintoul', 'Ritchie', 'Roana', 'Robert', 'Robyn', 'Rockie', 'Rodie', 'Roer', 'Rolando', 'Romanas', 'Romonda', 'Ronny', 'Rosa', 'Rosanne', 'Rosemare', 'Rosenthal', 'Rossen', 'Rothwell', 'Rowney', 'Roz', 'Ruberta', 'Rudin', 'Rufford', 'Ruperta', 'Russo', 'Ruthy', 'Saba', 'Sachi', 'Sadler', 'Saied', 'Salas', 'Sallee', 'Salvador', 'Sami', 'Sanborne', 'Sandry', 'Santa', 'Sarajane', 'Sartin', 'Saum', 'Savior', 'Saylor', 'Schaeffer', 'Scheider', 'Schlesinger', 'Schoening', 'Schriever', 'Schwartz', 'Scotti', 'Seaden', 'Sebastiano', 'Seem', 'Seiter', 'Selhorst', 'Selmner', 'Seow', 'Sergius', 'Seto', 'Seymour', 'Shakti', 'Shanie', 'Shargel', 'Shaughnessy', 'Shear', 'Shel', 'Shelton', 'Shere', 'Sherr', 'Sheya', 'Shippee', 'Shoifet', 'Shue', 'Shute', 'Sibley', 'Sidon', 'Siesser', 'Sik', 'Silsby', 'Simah', 'Sinclair', 'Sirotek', 'Skantze', 'Skipton', 'Slayton', 'Smart', 'So', 'Solberg', 'Sommer', 'Sophey', 'Sosna', 'Spalla', 'Spence', 'Spohr', 'Stacey', 'Stan', 'Stanton', 'Staten', 'Steele', 'Steinke', 'Stephenie', 'Stevena', 'Stillas', 'Stoecker', 'Stouffer', 'Streetman', 'Stroup', 'Stutsman', 'Sugihara', 'Sunda', 'Susana', 'Suzan', 'Swamy', 'Swetlana', 'Sybille', 'Synn', 'Tace', 'Taggart', 'Talbert', 'Tam', 'Tammie', 'Tannenbaum', 'Tarr', 'Tate', 'Tawney', 'Tedda', 'Tegan', 'Ten', 'Terbecki', 'Terrance', 'Tertia', 'Tews', 'Thanh', 'Thedrick', 'Therese', 'Thibaut', 'Thomajan', 'Thorma', 'Three', 'Tibbitts', 'Tiertza')
information = ('TeamLeader', 'Manager', 'AssistantManager', 'Executive', 'Director', 'Coordinator', 'Administrator', 'Controller', 'Officer', 'Organizer', 'Supervisor', 'Superintendent', 'Head', 'Overseer', 'Chief', 'Foreman', 'Controller', 'Principal', 'President', 'Lead', 'AdministrativeAssistant', 'Receptionist', 'OfficeManager', 'AuditingClerk', 'Bookkeeper', 'AccountExecutive', 'BranchManager', 'BusinessManager', 'QualityControlCoordinator', 'AdministrativeManager', 'ChiefExecutiveOfficer', 'BusinessAnalyst', 'RiskManager', 'HumanResources', 'OfficeAssistant', 'Secretary', 'OfficeClerk', 'FileClerk', 'AccountCollector', 'AdministrativeSpecialist', 'ExecutiveAssistant', 'ProgramAdministrator', 'ProgramManager', 'AdministrativeAnalyst', 'DataEntry', 'ComputerScientist', 'ITProfessional', 'UXDesigner&UIDeveloper', 'SQLDeveloper', 'WebDesigner', 'WebDeveloper', 'HelpDeskWorker/DesktopSupport', 'SoftwareEngineer', 'DataEntry', 'DevOpsEngineer', 'ComputerProgrammer', 'NetworkAdministrator', 'InformationSecurityAnalyst', 'ArtificialIntelligenceEngineer', 'CloudArchitect', 'ITManager', 'TechnicalSpecialist', 'ApplicationDeveloper', 'ChiefTechnologyOfficer(CTO)', 'ChiefInformationOfficer(CIO)', 'SalesAssociate', 'SalesRepresentative', 'SalesManager', 'RetailWorker', 'StoreManager', 'SalesRepresentative', 'SalesManager', 'RealEstateBroker', 'SalesAssociate', 'Cashier', 'StoreManager', 'AccountExecutive', 'AccountManager', 'AreaSalesManager', 'DirectSalesperson', 'DirectorofInsideSales', 'OutsideSalesManager', 'SalesAnalyst', 'MarketDevelopmentManager', 'B2BSalesSpecialist', 'SalesEngineer', 'MerchandisingAssociate', 'VirtualAssistant', 'CustomerService', 'CustomerSupport', 'Concierge', 'HelpDesk', 'CustomerServiceManager', 'TechnicalSupportSpecialist', 'AccountRepresentative', 'ClientServiceSpecialist', 'CustomerCareAssociate')
project_names = ('Activeattack', 'Activecyberdefence', 'Antivirus', 'Bacterium', 'BankerTrojan', 'Bankcardfraud', 'Behaviour', 'Blackhathacker', 'Blacklist', 'Blackmail', 'Botnet', 'Cyberattack', 'Cyberbullying', 'Cybercriminal', 'Cyberdetective', 'MetasploitUnleashed', 'PTES', 'OWASP', 'PENTEST-WIKI', 'PTF', 'XSS-Payloads', 'OSSTMM', 'MITRE(ATT&CK)', 'OSINTFramework', 'IntelTechniques', 'NetBootcampOSINTTools', 'WiGLE.net', 'SocialEngineeringFramework', 'ArchStrike', 'BlackArch-Arch', 'NetworkSecurityToolkit', 'Pentoo', 'BackBox', 'Parrot', 'Buscador', 'FedoraSecurityLab', 'Attifyos', 'Nexpose', 'Nessus', 'OpenVAS', 'Vuls', 'FindBugs', 'Sobelow', 'Bandit', 'Nmap', 'Ctf-tools', 'Pwntools', 'RsaCtfTool', 'CVE', 'CWE', 'CTF', 'Jora', 'Jira')
task_names = ('Настройка сканера уязвимостей', 'Включить сканер', 'Провести Пентест', 'Написать важную бумажку', 'Составить список задач', 'Взломать', 'Запустить брутфорс', 'Запустить фазинг директорий', 'Включить антивирус', 'Написать скрипт для автоматизации', 'Провести совещание внутри отдела', 'Поспать', 'Покушать', 'Организовать совещание')
task_description = ('Может показаться странным', 'Прототип нового сервиса', 'Цены начинают падать', 'Низкий приоритет', 'Случайный текст', 'Ни к чему не обязывает', 'Средняя по приоритету задача', 'Вообще не приоритетная задача', 'Смешно', 'Забей', 'Давайте разбираться', 'Органический трафик', 'Приоритетная задача', 'Мелочь, а приятно', 'Бэклог', 'Наивысший приоритет!', 'Можно не делать...', 'Сделай завтра', 'Сделай в следующем месяце', 'Сделай на следующей неделе')


def get_random_name():
    """
    Генерация рандомного имени пользователя для регистрации
    """
    ran = len(names)
    name = names[random.randint(0, ran - 1)]
    return name + str(random.randint(10000, 99999))


def get_random_info():
    """
    Генерация рандомной должности пользователя
    """
    ran = len(information)
    info = information[random.randint(0, ran - 1)]
    return info


def get_random_project_name():
    """
    Генерация рандомной должности пользователя
    """
    ran = len(project_names)
    name = project_names[random.randint(0, ran - 1)]
    return name


def get_random_task_name():
    """
    Генерация рандомной должности пользователя
    """
    ran = len(task_names)
    name = task_names[random.randint(0, ran - 1)]
    return name


def get_random_task_description():
    """
    Генерация рандомной должности пользователя
    """
    ran = len(task_description)
    desc = task_description[random.randint(0, ran - 1)]
    return desc


def get_password():
    """
    Генерация рандомного пароля для регистрации
    """
    password = []
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    for i in range(20):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)


def get_place_for_flag():
    """
    Куда класть флаг
    """
    if "PUSH_PLACE" in os.environ:
        return bool(int(os.environ.get("PUSH_PLACE")))
    number_of_spots = 2
    percentage = number_of_spots * 100
    place = secrets.choice(range(0, percentage))
    return place < percentage / 3


class Status(enum.Enum):
    OK = 101
    CORRUPT = 102
    MUMBLE = 103
    DOWN = 104
    ERROR = 110

    def __bool__(self):
        return self.value == Status.OK


class CheckerResult(NamedTuple):
    """
    Класс описывет результат работы чекера для push и pull
    """
    status: int
    private_info: str
    public_info: str


class PushArgs(NamedTuple):
    """
    Класс описывет аргументы для функции push
    """
    host: str  # хост на котором расположен сервис
    round_number: int  # номер текущего раунда
    flag: str  # флаг который нужно положить в сервис


class PullArgs(NamedTuple):
    """
    Класс описывет аргументы для функции pull
    """
    host: str  # хост на котором расположен сервис
    private_info: str  # приватные данные которые чекер вернул когда клал флаг
    flag: str  # Флаг который нужно получить из сервиса


def get_json(response, validate_response=True):
    """
    Проверка полученного json
    """
    try:
        data = json.loads(response.text)
    except:
        CheckerResult(status=Status.MUMBLE.value,
                      private_info=f'JSON validation error on url: {response.url}',
                      public_info=f'JSON validation error on url: {response.url}, content: {response.text}')
    if not validate_response:
        return data
    try:
        if response.status_code == 200:
            return data
        else:
            CheckerResult(status=Status.MUMBLE.value,
                          private_info=f'Response status not success on url: {response.url}',
                          public_info=f'Response status not success on url: {response.url}, content: {response.text}')
    except:
        CheckerResult(status=Status.MUMBLE.value,
                      private_info=f'Unknown response status ("success" field in response not found), url: {response.url}',
                      public_info=f'Unknown response status ("success" field in response not found), url: {response.url}, content: {response.text}')


def push(args: PushArgs) -> CheckerResult:
    """
    Функция PUSH
    """
    url = f'http://{args.host}:{PORT}/api'
    place_flag = get_place_for_flag()
    """if place_flag = True - flag will be in description, if = False - flag will be in attachment"""

    # Check push
    # Connect

    try:
        r = requests.get(f"{url}/register", headers={'User-Agent': rnd_agent()})
    except Exception as e:
        return CheckerResult(status=Status.DOWN.value,
                            private_info=str(e),
                            public_info=f'PUSH {Status.DOWN.value} Can not connect')

    try:
        creds_register_1 = {"username": get_random_name(), "password": get_password(), "info": get_random_info()}
        creds_login_1 = {"username": creds_register_1.get("username"), "password": creds_register_1.get("password")}

        creds_register_2 = {"username": get_random_name(), "password": get_password(), "info": get_random_info()}
        creds_login_2 = {"username": creds_register_2.get("username"), "password": creds_register_2.get("password")}
    except Exception as e:
        return CheckerResult(status=Status.ERROR.value,
                             private_info=str(e),
                             public_info=f'PUSH {Status.ERROR.value} checker can not generate creds')

    # Register главного и второстепенного пользователей
    try:
        r = requests.post(f'{url}/register', json=creds_register_1, headers={'User-Agent': rnd_agent()})
        print(r.status_code, r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                            private_info=str(e),
                            public_info=f'PUSH {Status.MUMBLE.value} can not register first user: {r.url}, content: {r.text}')

    try:
        r = requests.post(f'{url}/register', json=creds_register_2, headers={'User-Agent': rnd_agent()})
        print(r.status_code, r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                            private_info=str(e),
                            public_info=f'PUSH {Status.MUMBLE.value} can not register second user: {r.url}, content: {r.text}')

    # Login
    try:
        r = requests.post(f'{url}/login', json=creds_login_1, headers={'User-Agent': rnd_agent()})
        print(r.status_code, r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
        token = data["token"]
        print(token)
        auth_header = {'Authorization': f'Bearer {token}', 'User-Agent': rnd_agent()}
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                            private_info=str(e),
                            public_info=f'PUSH {Status.MUMBLE.value} can not login: {r.url}, content: {r.text}')

    # Get Profile data
    try:
        r = requests.get(f'{url}/profile', headers=auth_header)
        print(r.status_code, r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                            private_info=str(e),
                            public_info=f'PUSH {Status.MUMBLE.value} can not get profile data: {r.url}, content: {r.text}')

    # Get Projects data
    try:
        r = requests.get(f'{url}/open_projects', headers=auth_header)
        print(auth_header)
        print(r.status_code, r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                            private_info=str(e),
                            public_info=f'PUSH {Status.MUMBLE.value} can not get projects data: {r.url}, content: {r.text}')

    # Add new project
    try:
        if place_flag:
            description = args.flag
        else:
            description = ''
        r = requests.post(f'{url}/create_project', headers=auth_header,
                          json={"users": [creds_register_2.get("username")],
                                "new_project_data":
                                    {
                                        "name": get_random_project_name(),
                                        "description": description
                                    }
                                })
        print("response", r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        if r.json()["description"] != args.flag and place_flag:
            return CheckerResult(status=Status.CORRUPT.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.CORRUPT.value} Can not store flag')
        data = get_json(r)
        project_id = data["project_id"]
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                            private_info=str(e),
                            public_info=f'PUSH {Status.MUMBLE.value} can not create new project: {r.url}, content: {r.text}')

    # Create Task in project for second user
    try:
        r = requests.post(f'{url}/create_task?project_id={project_id}',
                         headers=auth_header,
                         json={"name": get_random_task_name(),
                               "description": get_random_task_description(),
                               "responsible": creds_register_2.get("username")})
        print("response", r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)

    # Upload file to attachment
        if place_flag:
            files = {'file': ('report'+str(args.round_number)+'.csv', '')}
        else:
            files = {'file': ('report'+str(args.round_number)+'.csv', args.flag)}
        r = requests.post(f'{url}/uploadfile?task_id={data["task_id"]}',
                          headers=auth_header,
                          files=files)
        print("response-upload-file", r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
        filename = data["attachments"][0]
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                            private_info=str(e),
                            public_info=f'PUSH {Status.MUMBLE.value} can not create task/upload file to attachments: {r.url}, content: {r.text}')

    # Create report
    try:
        r = requests.get(f'{url}/create_report?project_id={project_id}',
                         headers=auth_header)
        print("response-create-report", r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                         private_info=str(e),
                         public_info=f'PUSH {Status.MUMBLE.value} can not create report: {r.url}, content: {r.text}')

    # Download
    try:
        r = requests.get(f'{url}/download?filename={filename}',
                         headers=auth_header)
        print("response-download-file", r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        if r.text != args.flag and not place_flag:
            return CheckerResult(status=Status.CORRUPT.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.CORRUPT.value} Can not store flag')
        data = get_json(r)

    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                             private_info=str(e),
                             public_info=f'PUSH {Status.MUMBLE.value} can not create report: {r.url}, content: {r.text}')

    # Debug
    try:
        r = requests.get(f'{url}/debug?project_id={project_id}',
                         headers=auth_header)
        print("response-debug", r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                             private_info=str(e),
                             public_info=f'PUSH {Status.MUMBLE.value} can not create report: {r.url}, content: {r.text}')

    # Login second user
    try:
        r = requests.post(f'{url}/login', json=creds_login_2, headers={'User-Agent': rnd_agent()})
        print(r.status_code, r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
        token = data["token"]
        print(token)
        auth_header = {'Authorization': f'Bearer {token}', 'User-Agent': rnd_agent()}
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                             private_info=str(e),
                             public_info=f'PUSH {Status.MUMBLE.value} can not login under second user: {r.url}, content: {r.text}')

    # Get Projects data second user
    try:
        r = requests.get(f'{url}/open_projects', headers=auth_header)
        print(r.status_code, r.text)
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                 private_info=f'{r.status_code}',
                                 public_info=f'PUSH {Status.MUMBLE.value} {r.url} - {r.status_code}')
        data = get_json(r)
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                             private_info=str(e),
                             public_info=f'PUSH {Status.MUMBLE.value} can not get projects data of second user: {r.url}, content: {r.text}')

    if place_flag:
        private = creds_login_1 | {"flag_place": 1, "private": project_id}
    else:
        private = creds_login_1 | {"flag_place": 0, "private": filename}
    res = CheckerResult(status=Status.OK.value,
                        private_info=json.dumps(private),
                        public_info='PUSH works')
    return res


def pull(args: PullArgs) -> CheckerResult:
    res = CheckerResult(status=Status.OK.value,
                        private_info=str(args.private_info),
                        public_info='PULL works')

    url = f'http://{args.host}:{PORT}/api'
    print(args.private_info)
    creds = {"username": json.loads(args.private_info)["username"], "password": json.loads(args.private_info)["password"]}
    flag_place = {"flag_place": json.loads(args.private_info)["flag_place"], "private": json.loads(args.private_info)["private"]}

    # Login
    try:
        r = requests.post(f'{url}/login', json=creds, headers={'User-Agent': rnd_agent()})
        if r.status_code != 200:
            return CheckerResult(status=Status.MUMBLE.value,
                                private_info=str(args.private_info),
                                public_info=f'PULL {Status.MUMBLE.value} can not login {r.url} - {r.status_code}')
        data = get_json(r)
        token = data["token"]
        print(token)
        auth_header = {'Authorization': f'Bearer {token}', 'User-Agent': rnd_agent()}
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                             private_info=str(e),
                             public_info=f'PULL {Status.MUMBLE.value} can not login: {r.url}, content: {r.text}')

    # Check Flag
    try:
        if flag_place["flag_place"]:
            # check in project
            query = f'{url}/open_projects'
            r = requests.get(query, headers=auth_header)
            if r.status_code != 200:
                return CheckerResult(status=Status.MUMBLE.value,
                                     private_info=f'{r.status_code}',
                                     public_info=f'PULL {Status.MUMBLE.value} can not get flag: {r.url}, content: {r.text}')
            project = ''
            print("data", r.text)
            for i in range(len(json.loads(r.text))):
                if json.loads(r.text)[i]["project_id"] == flag_place["private"]:
                    project = json.loads(r.text)[i]
            if args.flag not in project["description"]:
                return CheckerResult(status=Status.CORRUPT.value,
                                     private_info=str(args.private_info),
                                     public_info=f'PULL {Status.CORRUPT.value} Flags do not match: {r.url}, content: {r.text}')
            # check in create report
            query = f'{url}/create_report?project_id={flag_place["private"]}'
            r = requests.get(query, headers=auth_header)
            print(r.status_code, r.text)
            if r.status_code != 200:
                return CheckerResult(status=Status.MUMBLE.value,
                                     private_info=f'{r.status_code}',
                                     public_info=f'PULL {Status.MUMBLE.value} can not get flag: {r.url}, content: {r.text}')
            project_data = r.text
            project_data = project_data[project_data.find('description=') + 13:project_data.find('creator=') - 2]
            if args.flag not in project_data:
                return CheckerResult(status=Status.CORRUPT.value,
                                     private_info=str(args.private_info),
                                     public_info=f'PULL {Status.CORRUPT.value} Flags do not match: {r.url}, content: {r.text}')
        else:
            query = f'{url}/download?filename={flag_place["private"]}'
            r = requests.get(query, headers=auth_header)
            print(r.status_code, r.text)
            if r.status_code != 200:
                return CheckerResult(status=Status.MUMBLE.value,
                                     private_info=f'{r.status_code}',
                                     public_info=f'PULL {Status.MUMBLE.value} can not get flag: {r.url}, content: {r.text}')
            print("data", r.text)
            if args.flag not in r.text:
                return CheckerResult(status=Status.CORRUPT.value,
                                     private_info=str(args.private_info),
                                     public_info=f'PULL {Status.CORRUPT.value} Flags do not match: {r.url}, content: {r.text}')
    except Exception as e:
        return CheckerResult(status=Status.MUMBLE.value,
                             private_info=str(e),
                             public_info=f'PULL {Status.MUMBLE.value} flags dont match: {r.url}, content: {r.text}')
    return res


if __name__ == '__main__':
    import sys
    action, *args = sys.argv[1:]
    result = None
    try:
        if action == 'push':
            host, round_number, flag = args
            push_args = PushArgs(host=host,round_number=round_number, flag=flag)
            # push_args.host, push_args.round_number, push_args.flag = args
            result = push(push_args)

        elif action =='pull':
            host, private_info, flag = args
            pull_args = PullArgs(host=host,private_info=private_info, flag=flag)
            result = pull(pull_args)
        else:
            result = CheckerResult(status=Status.ERROR.value, private_info='', public_info='No action found in args')
    except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
        result = CheckerResult(status=Status.DOWN.value, private_info='', public_info='Service is DOWN')
    except SystemError as e:
        raise
    except Exception as e:
        result = CheckerResult(status=Status.ERROR.value, private_info='', public_info=str(e))
    if result.status != Status.OK.value:
        print(result.public_info, file = sys.stderr)
    print(result.private_info)
    exit(result.status)