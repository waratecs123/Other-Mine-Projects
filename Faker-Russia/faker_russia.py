import random
import json
from datetime import datetime


class FakerRussia:
    def __init__(self, my_gender: str = None):
        self._load_all_data()

        if isinstance(my_gender, str) and len(my_gender) > 0 and my_gender in self.GENDER:
            self.my_gender = my_gender
        else:
            self.my_gender = None
        self._name = None
        self._surname = None
        self._patronymic = None
        self._father_name = None
        self._region = None
        self._city = None
        self._age = None
        self._year = None
        self._has_car = None
        self._work_experience = None

    def _load_json(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _load_all_data(self):
        other_data = self._load_json('data/other/other_data.json')
        self.GENDER = other_data.get("GENDER", ["male", "female"])
        self.TYPE_BUILDINGS = other_data.get("TYPE_BUILDINGS", ["д.", "корп."])
        self.WEIGHT_FACTORS_1 = other_data.get("WEIGHT_FACTORS_1", [7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
        self.WEIGHT_FACTORS_2 = other_data.get("WEIGHT_FACTORS_2", [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
        self.COUNTRY_CODE = other_data.get("COUNTRY_CODE", "+7")
        self.PREFIX = other_data.get("PREFIX")
        self.LEVEL_WORK = other_data.get("LEVEL_WORK", [])
        self.N_A = other_data.get("N_A", "N/A")

        female_names_data = self._load_json('data/female/female_name.json')
        self.FEMALE_NAMES = female_names_data.get("FEMALE_NAMES", [])

        female_surnames_data = self._load_json('data/female/female_surname.json')
        self.FEMALE_SURNAMES = female_surnames_data.get("FEMALE_SURNAMES", [])

        female_patronymics_data = self._load_json('data/female/female_patronymic.json')
        self.FEMALE_PATRONYMICS = female_patronymics_data.get("FEMALE_PATRONYMICS", {})

        male_names_data = self._load_json('data/male/male_name.json')
        self.MALE_NAMES = male_names_data.get("MALE_NAMES", [])

        male_surnames_data = self._load_json('data/male/male_surname.json')
        self.MALE_SURNAMES = male_surnames_data.get("MALE_SURNAMES", [])

        male_patronymics_data = self._load_json('data/male/male_patronymic.json')
        self.MALE_PATRONYMICS = male_patronymics_data.get("MALE_PATRONYMICS", {})

        regions_data = self._load_json('data/address/regions_cities_streets.json')
        self.REGIONS_CITIES_STREETS = regions_data.get("REGIONS_CITIES_STREETS", {})

        postal_codes_data = self._load_json('data/address/postal_codes.json')
        self.POSTAL_CODES = postal_codes_data.get("POSTAL_CODES", {})

        inn_data = self._load_json('data/inn/region_codes.json')
        self.CITY_TO_INN_PREFIX = inn_data.get("CITY_TO_INN_PREFIX", {})

        phone_data = self._load_json('data/phone/phone_code.json')
        self.PHONE_CODES = phone_data.get("PHONE_CODES", {})

        passport_data = self._load_json('data/passport/regions_codes.json')
        self.PASSPORT_REGION_CODES = passport_data.get("PASSPORT_REGION_CODES", {})

        nationality_data = self._load_json('data/nationality/nationality.json')
        self.NATIONALITIES = nationality_data.get("NATIONALITIES", [])

        email_usernames_data = self._load_json('data/email/email_usernames.json')
        self.EMAIL_USERNAMES = email_usernames_data.get("EMAIL_USERNAMES", [])

        email_domains_data = self._load_json('data/email/email_domains.json')
        self.EMAIL_DOMAINS = email_domains_data.get("EMAIL_DOMAINS", [])

        banks_data = self._load_json('data/bank/banks.json')
        self.BANKS = banks_data.get("BANKS", [])

        diseases_data = self._load_json('data/disease/diseases.json')
        self.DISEASES = diseases_data.get("DISEASES", [])

        jobs_data = self._load_json('data/job/jobs.json')
        self.JOBS = jobs_data.get("JOBS", [])

        employment_status_data = self._load_json('data/job/employment_status.json')
        self.EMPLOYMENT_STATUS = employment_status_data.get("EMPLOYMENT_STATUS", [])

        cars_data = self._load_json('data/car/cars.json')
        self.CARS = cars_data.get("CARS", {})

        regions_gos_codes_data = self._load_json('data/car/regions_gos_codes.json')
        self.REGIONS_GOS_CODES = regions_gos_codes_data.get("REGIONS_GOS_CODES", {})

        social_networks_messengers_data = self._load_json('data/social_networks_messengers/social_networks_messengers.json')
        self.SOCIAL_NETWORKS_AND_MESSENGERS = social_networks_messengers_data.get("SOCIAL_NETWORKS_AND_MESSENGERS", [])

    def reset(self):
        try:
            self.my_gender = None
            self._name = None
            self._surname = None
            self._patronymic = None
            self._father_name = None
            self._region = None
            self._city = None
            self._age = None
            self._year = None
            self._has_car = None
            self._work_experience = None

            return "Все данные были сброшены"
        except Exception:
            return "Данные не смогли сброситься"

    @property
    def age(self):
        try:
            if self._age is None:
                self._age = random.randint(1, 110)
                return self._age
            else:
                return self._age
        except Exception:
            return self.N_A

    @property
    def year(self):
        try:
            if self._year is None:
                now_year = datetime.now()
                month = str(now_year.month)
                day = str(now_year.day)

                if len(month) < 2:
                    month = f"0{now_year.month}"

                if len(day) < 2:
                    day = f"0{now_year.day}"

                year_answer = now_year.year - self.age

                if random.choice([True, False, False]):
                    self._year = f"{day}.{month}.{year_answer}"
                else:
                    month_1 = random.randint(1, 12)
                    day_1 = random.randint(1, 30)

                    if len(str(day_1)) < 2:
                        day_2 = f"0{day_1}"
                        day_1 = day_2

                    if month_1 > now_year.month:
                        year_answer -= 1

                    if len(str(month_1)) < 2:
                        month_2 = f"0{month_1}"
                        month_1 = month_2

                    self._year = f"{day_1}.{month_1}.{year_answer}"

                return self._year
            else:
                return self._year
        except Exception:
            return self.N_A

    @property
    def gender(self):
        try:
            if self.my_gender is None:
                self.my_gender = random.choice(self.GENDER)
                return self.my_gender
            else:
                return self.my_gender
        except Exception:
            return self.N_A

    @property
    def name(self):
        try:
            if self._name is None:
                if self.gender == self.GENDER[0]:
                    self._name = random.choice(self.MALE_NAMES)
                    return self._name
                else:
                    self._name = random.choice(self.FEMALE_NAMES)
                    return self._name
            else:
                return self._name
        except Exception:
            return self.N_A

    @property
    def surname(self):
        try:
            if self._surname is None:
                if self.gender == self.GENDER[0]:
                    self._surname = random.choice(self.MALE_SURNAMES)
                    return self._surname
                else:
                    self._surname = random.choice(self.FEMALE_SURNAMES)
                    return self._surname
            else:
                return self._surname
        except Exception:
            return self.N_A

    @property
    def patronymic(self):
        try:
            if self._patronymic is None:
                if self.gender == self.GENDER[0]:
                    self._patronymic = random.choice(list(self.MALE_PATRONYMICS.keys()))
                    return self._patronymic
                else:
                    self._patronymic = random.choice(list(self.FEMALE_PATRONYMICS.keys()))
                    return self._patronymic
            else:
                return self._patronymic
        except Exception:
            return self.N_A

    @property
    def full_name(self):
        try:
            return f"{self.surname} {self.name} {self.patronymic}"
        except Exception:
            return self.N_A

    @property
    def father_name(self):
        try:
            if self._father_name is None:
                if self.gender == self.GENDER[0]:
                    self._father_name = self.MALE_PATRONYMICS[self.patronymic]
                    return self._father_name
                else:
                    self._father_name = self.FEMALE_PATRONYMICS[self.patronymic]
                    return self._father_name
            else:
                return self._father_name
        except Exception:
            return self.N_A

    @property
    def full_name_father(self):
        try:
            try:
                name = self.father_name
                patronymic = random.choice(list(self.MALE_PATRONYMICS.keys()))

                if self.gender == self.GENDER[0]:
                    surname = self._surname
                else:
                    female_surname = self._surname
                    if female_surname.endswith('а'):
                        male_surname = female_surname[:-1]
                    else:
                        try:
                            idx = self.FEMALE_SURNAMES.index(female_surname)
                            male_surname = self.MALE_SURNAMES[idx]
                        except ValueError:
                            male_surname = female_surname
                    surname = male_surname

                return f"{surname} {name} {patronymic}"
            except Exception:
                return "Данных об отце не найдено"
        except Exception:
            return self.N_A

    @property
    def full_name_mother(self):
        try:
            try:
                name = random.choice(self.FEMALE_NAMES)
                patronymic = random.choice(list(self.FEMALE_PATRONYMICS.keys()))

                if self.gender == self.GENDER[0]:
                    male_surname = self._surname
                    try:
                        idx = self.MALE_SURNAMES.index(male_surname)
                        surname = self.FEMALE_SURNAMES[idx]
                    except ValueError:
                        surname = male_surname + 'а'
                else:
                    surname = self._surname

                maiden_name = random.choice(self.FEMALE_SURNAMES)
                return f"{surname} (девичья фамилия - {maiden_name}) {name} {patronymic}"
            except Exception:
                return "Данных о матери не найдено"
        except Exception:
            return self.N_A

    @property
    def region(self):
        try:
            if self._region is None:
                self._region = random.choice(list(self.REGIONS_CITIES_STREETS.keys()))
            return self._region
        except Exception:
            return self.N_A

    @property
    def city(self):
        try:
            if self._city is None:
                self._city = random.choice(list(self.REGIONS_CITIES_STREETS[self.region].keys()))
            return self._city
        except Exception:
            return self.N_A

    @property
    def street(self):
        try:
            return random.choice(self.REGIONS_CITIES_STREETS[self.region][self.city])
        except Exception:
            return self.N_A

    @property
    def registration_address(self):
        try:
            answer = f"{self.region} - Город {self.city} - {self.street}"
            first_building = self.TYPE_BUILDINGS[0]
            number_first_buildings = random.randint(1, 300)
            postal_code = self.POSTAL_CODES[self.city]
            text = ""
            if random.choice([True, False]):
                second_buildings = self.TYPE_BUILDINGS[1]
                number_second_buildings = random.randint(1, 50)
                text = f"{first_building} {number_first_buildings} {second_buildings} {number_second_buildings}"
                return f"{postal_code}, {answer} {text}"
            else:
                text = f"{first_building} {number_first_buildings}"
                return f"{postal_code}, {answer} {text}"
        except Exception:
            return self.N_A

    @property
    def actual_address(self) -> str:
        try:
            if random.random() < 0.3:
                return "Совпадает с адресом регистрации"
            else:
                if random.choice([True, False]):
                    other_street = random.choice(self.REGIONS_CITIES_STREETS[self.region][self.city])

                    while other_street == self.street and len(self.REGIONS_CITIES_STREETS[self.region][self.city]) > 1:
                        other_street = random.choice(self.REGIONS_CITIES_STREETS[self.region][self.city])

                    other_postal_code = self.POSTAL_CODES[self.city]
                    building = random.randint(1, 300)
                    return f"{other_postal_code}, {self.region} - Город {self.city} - {other_street} д. {building}"
                else:
                    other_region = random.choice(list(self.REGIONS_CITIES_STREETS.keys()))
                    other_city = random.choice(list(self.REGIONS_CITIES_STREETS[other_region].keys()))
                    other_street = random.choice(self.REGIONS_CITIES_STREETS[other_region][other_city])
                    building = random.randint(1, 300)
                    other_postal_code_1 = self.POSTAL_CODES[other_city]

                    return f"{other_postal_code_1}, {other_region} - Город {other_city} - {other_street} д. {building}"
        except Exception:
            return self.N_A

    @property
    def inn(self) -> str:
        try:
            first_4_numbers = self.CITY_TO_INN_PREFIX[self.city]

            sec_6_num = random.randint(0, 999999)
            second_6_numbers = str(sec_6_num).zfill(6)

            first_10 = list(first_4_numbers + second_6_numbers)
            first_10_digits = [int(d) for d in first_10]

            sum_11 = 0
            for i in range(10):
                sum_11 += first_10_digits[i] * self.WEIGHT_FACTORS_1[i]

            digit_11 = sum_11 % 11
            if digit_11 > 9:
                digit_11 = digit_11 % 10

            first_11_digits = first_10_digits + [digit_11]

            sum_12 = 0
            for i in range(11):
                sum_12 += first_11_digits[i] * self.WEIGHT_FACTORS_2[i]

            digit_12 = sum_12 % 11
            if digit_12 > 9:
                digit_12 = digit_12 % 10

            return f"{first_4_numbers}{second_6_numbers}{digit_11}{digit_12}"
        except Exception:
            return self.N_A

    @property
    def snils(self) -> str:
        try:
            fir_9_num = random.randint(100000000, 999999999)
            first_9_number = list(str(fir_9_num))
            lst_9 = []

            position = 9
            for digit in first_9_number:
                lst_9.append(position * int(digit))
                position -= 1

            control_number = sum(lst_9) % 101

            if control_number == 100:
                control_number = 0

            return (f"{''.join(first_9_number[0:3])}-{''.join(first_9_number[3:6])}"
                    f"-{''.join(first_9_number[6:9])} {control_number:02d}")
        except Exception:
            return self.N_A

    @property
    def phone(self) -> str:
        try:
            phone_code = self.PHONE_CODES[self.city]
            return (f"{self.COUNTRY_CODE} ({phone_code}) {random.randint(100, 999)}-"
                    f"{random.randint(10, 99)}-{random.randint(10, 99)}")
        except Exception:
            return self.N_A

    @property
    def passport_series_number(self) -> str:
        try:
            if self.age < 14:
                return "У данного гражданина ещё нет паспорта"

            first_2_number = self.PASSPORT_REGION_CODES[self.city]
            second_2_number = random.randint(1, 96)
            third_6_number = random.randint(100000, 999999)

            if len(str(second_2_number)) < 2:
                sec_2_num = f"0{second_2_number}"
                second_2_number = sec_2_num

            return f"{first_2_number} {second_2_number} {third_6_number}"
        except Exception:
            return self.N_A

    @property
    def date_issue(self) -> str:
        try:
            if self.age < 14:
                return "У данного гражданина ещё нет паспорта"

            year_issues = self.year.split(".")
            int_issues = int(year_issues[2])
            month = int(year_issues[1])
            waiting_time = random.randint(0, 14)
            day = int(year_issues[0]) + waiting_time

            if day > 30:
                day -= 30
                month += 1

            if month > 12:
                month -= 12
                int_issues += 1

            if len(str(month)) < 2:
                month_1 = f"0{month}"
                month = month_1

            if len(str(day)) < 2:
                day_1 = f"0{day}"
                day = day_1

            year_answer = ""

            if 14 <= self.age < 20:
                answer = int_issues + 14
                year_answer = f"{day}.{month}.{answer}"
            elif 20 <= self.age < 45:
                answer = int_issues + 20
                year_answer = f"{day}.{month}.{answer}"
            else:
                answer = int_issues + 45
                year_answer = f"{day}.{month}.{answer}"

            return year_answer
        except Exception:
            return self.N_A

    @property
    def unit_code(self) -> str:
        try:
            if self.age < 14:
                return "У данного гражданина ещё нет паспорта"

            text = f"{self.PASSPORT_REGION_CODES[self.city]}{random.randint(1000, 9999)}"
            mid = len(text) // 2
            final_text = f"{text[mid:]}-{text[:mid]}"
            return final_text
        except Exception:
            return self.N_A

    @property
    def nationality(self) -> str:
        try:
            return random.choice(self.NATIONALITIES)
        except Exception:
            return self.N_A

    @property
    def bik(self) -> str:
        try:
            return f"04{self.PASSPORT_REGION_CODES[self.city]}0{random.randint(0, 9)}{random.randint(100, 999)}"
        except Exception:
            return self.N_A

    @property
    def enp(self) -> str:
        first_1_number = 2
        second_23_number = self.PASSPORT_REGION_CODES[self.city]

        unique_part = [random.randint(0, 9) for _ in range(12)]

        first_15_digits = [first_1_number] + [int(d) for d in str(second_23_number).zfill(2)] + unique_part

        def calculate_luhn(digits):
            temp_digits = digits.copy()
            for i in range(len(temp_digits) - 1, -1, -2):
                temp_digits[i] *= 2
                if temp_digits[i] > 9:
                    temp_digits[i] -= 9
            total = sum(temp_digits)
            return (10 - (total % 10)) % 10

        checksum = calculate_luhn(first_15_digits)

        return ''.join(map(str, first_15_digits + [checksum]))

    @property
    def email(self) -> str:
        try:
            return f"{random.choice(self.EMAIL_USERNAMES)}@{random.choice(self.EMAIL_DOMAINS)}"
        except Exception:
            return self.N_A

    @property
    def bank(self) -> str:
        try:
            return random.choice(self.BANKS)
        except Exception:
            return self.N_A

    @property
    def diseases(self) -> str:
        try:
            if random.random() < 0.1:
                return "Болезни отсутствуют"
            else:
                diseases_lst = []
                for dis in range(random.randint(1, 4)):
                    diseases_lst.append(random.choice(self.DISEASES))
                return ", ".join(diseases_lst)
        except Exception:
            return self.N_A

    @property
    def job(self) -> str:
        try:
            if self.age < 18:
                return "Официальной работы ещё нет, человек несовершеннолетний"

            if ((self.gender == self.GENDER[0] and self.age >= 64) or
                (self.gender == self.GENDER[1] and self.age >= 59)):
                return "Человек на пенсии"

            if random.choice([True, False]):
                return random.choice(self.JOBS)
            else:
                return random.choice(self.EMPLOYMENT_STATUS)
        except Exception:
            return self.N_A

    @property
    def work_experience(self):
        try:
            if self.age < 18:
                self._work_experience = 0
                return "Официальной работы ещё нет, человек несовершеннолетни"

            getting_started = random.randint(18, 25)
            remains = self.age - getting_started

            if self.gender == self.GENDER[0] and self.age < 64:
                self._work_experience = remains
                return remains
            else:
                remains = 64 - getting_started

            if self.gender == self.GENDER[1] and self.age < 59:
                self._work_experience = remains
                return remains
            else:
                remains = 59 - getting_started

            self._work_experience = remains
            return remains
        except Exception:
            return self.N_A

    @property
    def car(self) -> str:
        try:
            if self.age < 16:
                self._has_car = False
                return "Нет доступного возраста, чтобы иметь машину"

            if random.choice([True, False]):
                car_brand = random.choice(list(self.CARS.keys()))
                car_model = random.choice(list(self.CARS[car_brand]))
                self._has_car = True
                return car_model
            else:
                self._has_car = False
                return "У данного человека нет машины"
        except Exception:
            return self.N_A

    @property
    def car_registration_number(self) -> str:
        try:
            if self._has_car:
                region_code = random.choice(self.REGIONS_GOS_CODES[self.region])
                numbers = random.randint(1, 999)
                str_num = len(str(numbers))
                letter_lst = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]

                if str_num < 3:
                    answer = (3 - str_num) * "0"
                    numbers_1 = answer + str(numbers)
                    numbers = numbers_1

                first_let = random.choice(letter_lst)
                second_let = random.choice(letter_lst)
                third_let = random.choice(letter_lst)

                return f"{first_let}{numbers}{second_let}{third_let} {region_code}"
            else:
                return "У данного гражданина ещё нет машины"
        except Exception:
            return self.N_A

    @property
    def shoe_size(self) -> str:
        try:
            if self.age >= 18:
                if self.gender == self.GENDER[0]:
                    return f"{random.randint(38, 50)}"
                else:
                    return f"{random.randint(33, 46)}"
            else:
                return f"{random.randint(20, 39)}"
        except Exception:
            return self.N_A

    @property
    def social_network_messenger(self):
        try:
            social_lst = []
            random_range = random.randint(1, 15)

            for _ in range(random_range):
                answer = random.choice(self.SOCIAL_NETWORKS_AND_MESSENGERS)
                if not answer in social_lst:
                    social_lst.append(answer)

            return ", ".join(social_lst)
        except Exception:
            return self.N_A

    @property
    def bank_card(self):
        try:
            eleven_num = random.randint(10000, 99999999999)
            eleven_num_str = str(eleven_num)

            if len(eleven_num_str) < 11:
                remainder = "0" * (11 - len(eleven_num_str))
                eleven_num = remainder + eleven_num_str
            else:
                eleven_num = eleven_num_str

            el_lst = list(self.PREFIX + str(eleven_num))
            index = 1
            answer_lst = []

            for i in el_lst:
                i = int(i)
                if index % 2 == 0:
                    i *= 2
                if i > 9:
                    i -= 9
                answer_lst.append(i)
                index += 1

            example_answer = sum(answer_lst)
            exp_an = example_answer % 10

            if not exp_an == 0:
                number_cycle = example_answer
                while True:
                    number_cycle += 1
                    if number_cycle % 10 == 0:
                        break
                return f"{self.PREFIX}{eleven_num}{number_cycle - example_answer}"
            else:
                return f"{self.PREFIX}{eleven_num}0"
        except Exception:
            return self.N_A

    @property
    def level_work(self):
        try:
            if self.work_experience == 0:
                return self.LEVEL_WORK[0]
            elif 0 < self.work_experience <= 2:
                return self.LEVEL_WORK[1]
            elif 2 < self.work_experience <= 5:
                return self.LEVEL_WORK[2]
            elif 5 < self.work_experience <= 9:
                return self.LEVEL_WORK[3]
            elif 9 < self.work_experience <= 12:
                return self.LEVEL_WORK[4]
            else:
                return self.LEVEL_WORK[5]
        except Exception:
            return self.N_A

    def __str__(self) -> str:
        return (f"ФИО: {self.full_name}\n"
                f"Год рождения: {self.year}\n"
                f"Возраст: {self.age}\n"
                f"Гендер(пол): {self.gender}\n"
                f"ФИО отца: {self.full_name_father}\n"
                f"ФИО матери: {self.full_name_mother}\n"
                f"Адрес регистрации: {self.registration_address}\n"
                f"Фактический адрес: {self.actual_address}\n"
                f"Номер телефона: {self.phone}\n"
                f"ИНН: {self.inn}\n"
                f"СНИЛС: {self.snils}\n"
                f"Серия и номер паспорта: {self.passport_series_number}\n"
                f"Дата выдачи паспорта: {self.date_issue}\n"
                f"Код подразделения: {self.unit_code}\n"
                f"Национальность: {self.nationality}\n"
                f"БИК: {self.bik}\n"
                f"Банк: {self.bank}\n"
                f"Номер банковской карты: {self.bank_card}\n"
                f"Единый номер полиса: {self.enp}\n"
                f"Электронная почта: {self.email}\n"
                f"Болезни: {self.diseases}\n"
                f"Работа: {self.job}\n"
                f"Стаж работы: {self.work_experience}\n"
                f"Уровень работы: {self.level_work}\n"
                f"Машина: {self.car}\n"
                f"Регистрационный номер машины: {self.car_registration_number}\n"
                f"Размер обуви: {self.shoe_size}\n"
                f"Социальные сети и мессенджеры: {self.social_network_messenger}\n")

if __name__ == "__main__":
    for answer in range(5):
        faker_russia_1 = FakerRussia()
        print(faker_russia_1)