import wikipediaapi


class GeneratorEngine:
    jobs = list()
    diseases = list()
    hobbies = list()
    human_traits = list()
    phobias = list()
    catastrophes = list()
    wiki = wikipediaapi.Wikipedia("ru")

    @staticmethod
    def get_from_wiki_by_category(category):
        ans = list()
        wiki = wikipediaapi.Wikipedia("ru")
        page_py = wiki.page(category)
        for page in page_py.categorymembers:
            pattern = r':'
            if not re.search(pattern, page):
                summary = wiki.page(page).summary
                # if len(summary) < 400:
                ans.append((page, summary))
        return ans

    def init_jobs_wiki(self):
        self.jobs = self.get_from_wiki_by_category("Категория:Профессии")

    def init_health_wiki(self):
        self.diseases = self.get_from_wiki_by_category("Категория:Заболевания_по_алфавиту")

    def init_biological_characteristics(self):
        pass

    def init_additional_skills(self):
        pass

    def init_human_character(self):
        self.human_traits = self.get_from_wiki_by_category("Категория:Черты_личности")

    def init_hobbies(self):
        self.hobbies = self.get_from_wiki_by_category("Категория:Хобби")

    def init_phobias(self):
        page = self.wiki.page("Список_фобий")
        # print(page.sections)
        letter = "А"
        for i in range(32):
            section = page.section_by_title(letter)
            if section:
                lines = section.text.split(sep='\n')
                for phobia in lines:
                    if len(phobia) > 0:
                        name, summary = phobia.split(sep=' — ', maxsplit=1)
                        self.phobias.append((name, summary))
            letter = chr(ord(letter) + 1)

    def init_special_conditions(self):
        pass

    def init_catastrophe(self):
        categories = ("Категория:Природные_катастрофы", "Категория:Техногенные_катастрофы", "Категория:Экологические_катастрофы")
        for category in categories:
            self.catastrophes += self.get_from_wiki_by_category(category)