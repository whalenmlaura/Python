import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import Ui_CountriesoftheWorld
from PyQt5.QtGui import QPixmap
class MyForm(QMainWindow, Ui_CountriesoftheWorld.Ui_MainWindow):

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)

        # ADD SLOTS HERE, indented to this level
        self.countries = {}
        self.ListWidget_Countries.itemClicked.connect(self.country_selected)
        self.Action_LoadCountries.triggered.connect(self.load_countries)
        self.ListWidget_Countries.itemClicked.connect(self.display_country_data)
        self.Box_SqUnits.currentIndexChanged.connect(self.convert_sq_units)
        self.RadioButton_SqKM.clicked.connect(self.km_pop_density)
        self.RadioButton_SqMile.clicked.connect(self.miles_pop_density)
        self.Button_UpdatePopulation.clicked.connect(self.update_population)

    # ADD SLOT FUNCTIONS HERE
    def country_selected(self, selected_country_index):
        str_CountryName = selected_country_index.text()
        str_CountryName = str_CountryName.replace(" ","_")
        self.Label_CountryName.setText(selected_country_index.text())
        imagePixmap = QPixmap(f"Flags\{str_CountryName}")
        self.Label_CountryFlag.setScaledContents(True)
        self.Label_CountryFlag.setPixmap(imagePixmap)
        
    def load_countries(self):
        country_file = open("countries.txt")
        self.countries = {}
        for line in country_file:
            line = line.replace("\n","")
            linelist = line.split(",")
            self.ListWidget_Countries.addItem(linelist[0])
            self.countries[linelist[0]] = linelist[1:]
        country_file.close()

    def update_population(self):
        country_data = self.countries
        str_Country = self.ListWidget_Countries.currentItem().text()
        population = int(country_data[str_Country][0])
        updated_pop = ""
        try:
            updated_pop = self.LineEdit_Population.text()
            updated_pop = updated_pop.replace(",","")
            updated_pop = int(updated_pop)
        except ValueError:
            QMessageBox.information(self, "Error","Invalid! Only numbers can be accepted")
            updated_pop = str(country_data[str_Country][0])
            updated_pop = f"{int(updated_pop):,}"
            self.LineEdit_Population.setText(updated_pop)
        else:
            self.countries[str_Country][0] = str(updated_pop)
            updated_pop = f"{int(updated_pop):,}"
            self.LineEdit_Population.setText(updated_pop)
            QMessageBox.information(self, "Updated","Population updated!")
        self.display_country_data(self.ListWidget_Countries.currentItem())

    def display_country_data(self, selected_country_index):
        country_data = self.countries
        str_Country = selected_country_index.text()
        population = f"{int(country_data[str_Country][0]):,}"
        self.LineEdit_Population.setText(population)
        area = f"{float(country_data[str_Country][1]):,.2f}"
        self.Label_TotalArea.setText(area)
        area_index = self.Box_SqUnits.currentIndex()
        set_area = self.convert_sq_units(area_index)
        self.Label_TotalArea.setText(set_area)
        isKM = self.RadioButton_SqKM.isChecked()
        isMiles = self.RadioButton_SqMile.isChecked()
        if isKM == True:
            self.km_pop_density(isKM)
        elif isMiles == True:
            self.miles_pop_density(isMiles)
        set_world_pop = self.world_pop_percent()
        world_pop = f"{set_world_pop:.4f}%"
        self.Label_PopulationPercentage.setText(world_pop)

    def convert_sq_units(self, selected_units):
        country_data = self.countries
        str_Country = self.ListWidget_Countries.currentItem().text()
        if selected_units == 0:
            area = f"{float(country_data[str_Country][1]):,.2f}"
            self.Label_TotalArea.setText(area)
            return area
        elif selected_units == 1:
            area = (float(country_data[str_Country][1])) * 2.589988
            km_area = f"{(area):,.2f}"
            self.Label_TotalArea.setText(km_area)
            return km_area
    
    def miles_pop_density(self, den_units):
        country_data = self.countries
        str_Country = self.ListWidget_Countries.currentItem().text()
        if den_units == 1:
            for c, data in country_data.items():
                if c == str_Country:
                    area = float(country_data[c][1])
                    population = float(country_data[c][0])
                    pop_density = (population/area)
                    pop_density = f"{pop_density:.2f}"
                    self.Label_PopulationDensity.setText(pop_density)

    def km_pop_density(self, den_units):
        country_data = self.countries
        str_Country = self.ListWidget_Countries.currentItem().text()
        if den_units == 1:
            for c, data in country_data.items():
                if c == str_Country:
                    area = (float(country_data[c][1]) * 2.589988)
                    population = float(country_data[c][0])
                    pop_density = (population/area)
                    pop_density = f"{pop_density:.2f}"
                    self.Label_PopulationDensity.setText(pop_density)

    def world_pop_percent(self):
        country_data = self.countries
        str_Country = self.ListWidget_Countries.currentItem().text()
        world_pop = 0
        for p, data in country_data.items():
            world_pop += float(country_data[p][0])
        population = float(country_data[str_Country][0])
        pop_percent = ((population / world_pop) * 100)
        return pop_percent
    
# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())