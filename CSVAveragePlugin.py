class CSVAveragePlugin:
    def input(self, filename):
        myfile = open(filename, 'r')
        self.firstline = myfile.readline()
        self.ADJ = []
        for line in myfile:
           contents = line.strip().split(',')
           for i in range(1, len(contents)):
               contents[i] = float(contents[i])
           self.ADJ.append(contents)

    def run(self):
        self.averages = ["Average"]
        for j in range(1, len(self.ADJ[0])):
            sum = 0
            for i in range(len(self.ADJ)):
               sum += self.ADJ[i][j]
            self.averages.append(sum/len(self.ADJ))


    def output(self, filename):
        outfile = open(filename, 'w')
        outfile.write(self.firstline)
        for i in range(len(self.averages)):
            outfile.write(str(self.averages[i]))
            if (i != len(self.averages)-1):
                outfile.write(',')
