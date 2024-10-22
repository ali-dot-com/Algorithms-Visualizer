import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
# from matplotlib.widgets import *
# from PyQt5.QtWidgets import QMessageBox
import sys
from ucs import UCS
from bfs import BFS
from dfs import DFS
from Astar import AStar
from AlphaBeta import AlphaBeta

DG = nx.DiGraph()
G = nx.Graph()
Goal_list = []


class Ui_AISearchingTechniquesMainWindow(object):
    counter = 0
    counterG = 0
    EdgeWeight_arr = [1] * 30
    HeuristicDict = dict()
    H = {}

    def GeneratePathClicked(self):
        original_stdout = sys.stdout  # Save a reference to the original standard output

        with open('test.txt', 'w') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            searchType = str(self.SearchTypecomboBox.currentText())
            graphType = str(self.GraphTypecomboBox.currentText())
            start = self.startingNode.text()
            goal = Goal_list

            if (graphType == "Undirectd Graph"):
                if searchType == "BFS":
                    graphbfs = BFS(G, graphType)
                    bfsPath = graphbfs.bfs(start, goal)
                    if (bfsPath):
                        print('BFS Path: ', end=' ')
                        graphbfs.bfsTraversal(bfsPath)
                        Goal_list.clear()
                    else :
                        print('Path Does not Exist')
                elif searchType == "DFS":
                    graphdfs = DFS(G, graphType)
                    dfsPath = graphdfs.dfs(start, goal)
                    if dfsPath:
                        print("DFS: Path: ", end = ' ')
                        graphdfs.dfsTraversal(dfsPath)
                        Goal_list.clear()
                    else:
                        print("Path Does not exist")

                elif searchType == "UCS":
                    graphucs = UCS(G)
                    path = graphucs.ucs(Goal_list, StartNode)

                    nx.draw_networkx(path)
                    plt.show()

                elif searchType == "A*":
                    graphAstar = AStar(G)
                    path = graphAstar.aStar(Goal_list, StartNode, self.H)
                    nx.draw_networkx(path)
                    plt.show()

                elif searchType == "Alpha-Beta":
                    graphAlphaBeta = AlphaBeta(G, self.H)
                    graph = graphAlphaBeta.alphaBeta(StartNode, self.H)
                    labels = nx.get_node_attributes(graph, 'val')
                    nx.draw_networkx(graph, labels = labels)
                    plt.show()

            else:       #for directed graph
                if searchType == "BFS":
                    graphbfs = BFS(G, graphType)
                    start = self.startingNode.text()
                    goals = Goal_list
                    bfsPath = graphbfs.bfs(start, goals)
                    if (bfsPath):
                        print('Path:', end=' ')
                        graphbfs.bfsTraversal(bfsPath)
                        print()
                        Goal_list.clear()
                    else:
                        print('Path Does not Exist')
                elif searchType == "DFS":
                    graphdfs = DFS(G, graphType)
                    # start = self.startingNode.text()
                    # goal = Goal_list
                    dfsPath = graphdfs.dfs(start, goal)
                    if dfsPath:
                        print("DFS: Path: ", end = ' ')
                        graphdfs.dfsTraversal(dfsPath)
                        Goal_list.clear()
                    else:
                        print("Path Does not exist")

        sys.stdout = original_stdout  # Reset the standard output to its original value

        with open("test.txt") as f:
            contents = f.read()
        self.TheResult_Label.setText(contents)

    def GenerateGraphClicked(self):
        if self.GraphTypecomboBox.currentText() == "Undirectd Graph":
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=1000)
            nx.draw_networkx_edge_labels(G, pos, font_size=16, edge_labels=nx.get_edge_attributes(G, 'weight'))
            plt.show()
        elif self.GraphTypecomboBox.currentText() == "Directed Graph":
            pos = nx.spring_layout(DG)
            nx.draw(DG, pos, with_labels=True, node_size=1000)
            nx.draw_networkx_edge_labels(DG, pos, font_size=16, edge_labels=nx.get_edge_attributes(DG, 'weight'))
            plt.show()

    def AddNodeClicked(self):
        N1 = self.Node1_input.text()
        N2 = self.Node2_input.text()
        weight = self.EdgeWieght_input.text()
        W = int(weight) if weight != "" else 1
        G.add_edge(N1, N2, weight=W)
        DG.add_edge(N1, N2, weight=W)

        self.EdgeWeight_arr[self.counter] = W
        self.counter = self.counter + 1
        self.Node1_input.clear()
        self.Node2_input.clear()
        self.EdgeWieght_input.clear()

    def HeuristicPushed(self):
        InputHeuristic = int(self.NodeHeuristic_input.text())
        InputNodeH = self.Node_Input.text()
        self.H[self.Node_Input.text()] = int(self.NodeHeuristic_input.text())
        # self.HeuristicDict.update({InputNodeH: InputHeuristic})
        # self.graphfirst.set_heuristics(self.HeuristicDict)
        # self.graphfirst2.set_heuristics(self.HeuristicDict)
        # self.graphastar1.set_heuristics(self.HeuristicDict)
        # self.graphastar2.set_heuristics(self.HeuristicDict)
        self.Node_Input.clear()
        self.NodeHeuristic_input.clear()


    def SubmitClicked(self):
        G = self.GoalNode_input.text()
        Goal_list.append(G)
        global StartNode
        StartNode = self.startingNode.text()
        self.GoalNode_input.clear()
        self.startingNode.clear()

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("AI Project")
        mainWindow.resize(770, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SearchTypecomboBox.setGeometry(QtCore.QRect(630, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SearchTypecomboBox.setFont(font)
        self.SearchTypecomboBox.setObjectName("SearchTypecomboBox")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.GenerateGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateGraphButton.setGeometry(QtCore.QRect(630, 240, 131, 31))
        self.GenerateGraphButton.setObjectName("GenerateGraphButton")
        self.GenerateGraphButton.clicked.connect(self.GenerateGraphClicked)
        self.Node1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1_input.setGeometry(QtCore.QRect(26, 48, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1_input.setFont(font)
        self.Node1_input.setText("")
        self.Node1_input.setObjectName("Node1_input")
        self.Node2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2_input.setGeometry(QtCore.QRect(26, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2_input.setFont(font)
        self.Node2_input.setObjectName("Node2_input")
        self.Node1Label = QtWidgets.QLabel(self.centralwidget)
        self.Node1Label.setGeometry(QtCore.QRect(26, 25, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1Label.setFont(font)
        self.Node1Label.setObjectName("Node1Label")
        self.Node2Label = QtWidgets.QLabel(self.centralwidget)
        self.Node2Label.setGeometry(QtCore.QRect(26, 78, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2Label.setFont(font)
        self.Node2Label.setObjectName("Node2Label")
        self.EdgeWieghtLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdgeWieghtLabel.setGeometry(QtCore.QRect(26, 131, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieghtLabel.setFont(font)
        self.EdgeWieghtLabel.setObjectName("EdgeWieghtLabel")
        self.EdgeWieght_input = QtWidgets.QLineEdit(self.centralwidget)
        self.EdgeWieght_input.setGeometry(QtCore.QRect(26, 157, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieght_input.setFont(font)
        self.EdgeWieght_input.setObjectName("EdgeWieght_input")
        self.AddNodesButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodesButton.setGeometry(QtCore.QRect(26, 189, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodesButton.setFont(font)
        self.AddNodesButton.setObjectName("AddNodesButton")
        self.AddNodesButton.clicked.connect(self.AddNodeClicked)
        self.TheResult_Label = QtWidgets.QLabel(self.centralwidget)
        # self.TheResult_Label.setGeometry(QtCore.QRect(10, 280, 751, 481))
        self.TheResult_Label.setGeometry(QtCore.QRect(10, 280, 750, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TheResult_Label.setFont(font)
        self.TheResult_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.TheResult_Label.setLineWidth(2)
        self.TheResult_Label.setText("")
        self.TheResult_Label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.TheResult_Label.setObjectName("TheResult_Label")
        self.GeneratePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.GeneratePathButton.setGeometry(QtCore.QRect(460, 240, 131, 31))
        self.GeneratePathButton.setObjectName("GeneratePathButton")
        self.GeneratePathButton.clicked.connect(self.GeneratePathClicked)
        self.TheResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.TheResultLabel.setGeometry(QtCore.QRect(10, 230, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TheResultLabel.setFont(font)
        self.TheResultLabel.setObjectName("TheResultLabel")
        self.Node_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node_Input.setGeometry(QtCore.QRect(227, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node_Input.setFont(font)
        self.Node_Input.setText("")
        self.Node_Input.setObjectName("Node_Input")
        self.NodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeLabel.setGeometry(QtCore.QRect(227, 26, 33, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeLabel.setFont(font)
        self.NodeLabel.setObjectName("NodeLabel")
        self.NodeHeuristicLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeHeuristicLabel.setGeometry(QtCore.QRect(227, 78, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristicLabel.setFont(font)
        self.NodeHeuristicLabel.setObjectName("NodeHeuristicLabel")
        self.NodeHeuristic_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NodeHeuristic_input.setGeometry(QtCore.QRect(227, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristic_input.setFont(font)
        self.NodeHeuristic_input.setObjectName("NodeHeuristic_input")
        self.AddNodeHeuristicButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodeHeuristicButton.setGeometry(QtCore.QRect(227, 130, 117, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodeHeuristicButton.setFont(font)
        self.AddNodeHeuristicButton.setObjectName("AddNodeHeuristicButton")
        self.AddNodeHeuristicButton.clicked.connect(self.HeuristicPushed)
        self.startingNode = QtWidgets.QLineEdit(self.centralwidget)
        self.startingNode.setGeometry(QtCore.QRect(430, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.startingNode.setFont(font)
        self.startingNode.setText("")
        self.startingNode.setObjectName("StartNode_input")
        self.StartNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartNodeLabel.setGeometry(QtCore.QRect(430, 26, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNodeLabel.setFont(font)
        self.StartNodeLabel.setObjectName("StartNodeLabel")
        self.GoalNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.GoalNodeLabel.setGeometry(QtCore.QRect(430, 77, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNodeLabel.setFont(font)
        self.GoalNodeLabel.setObjectName("GoalNodeLabel")
        self.GoalNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.GoalNode_input.setGeometry(QtCore.QRect(430, 100, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNode_input.setFont(font)
        self.GoalNode_input.setObjectName("GoalNode_input")
        self.GraphTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.GraphTypecomboBox.setGeometry(QtCore.QRect(630, 100, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GraphTypecomboBox.setFont(font)
        self.GraphTypecomboBox.setObjectName("GraphTypecomboBox")
        self.GraphTypecomboBox.addItem("")
        self.GraphTypecomboBox.addItem("")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(430, 150, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.SubmitClicked)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")

        self.TheResult_Label.setStyleSheet("background-color: white")
        
        # Set the label colors
        self.TheResultLabel.setStyleSheet("color: rgb(53, 123, 214); font-weight: 600")
        self.Node1Label.setStyleSheet("color: black;")
        self.Node2Label.setStyleSheet("color: black;")
        self.EdgeWieghtLabel.setStyleSheet("color: black;")
        self.NodeLabel.setStyleSheet("color: black;")
        self.NodeHeuristicLabel.setStyleSheet("color: black;")
        self.StartNodeLabel.setStyleSheet("color: black;")
        self.GoalNodeLabel.setStyleSheet("color: black;")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, AISearchingTechniquesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AISearchingTechniquesMainWindow.setWindowTitle(
            _translate("AI Project", "AI Project"))
        self.SearchTypecomboBox.setCurrentText(_translate("AI Project", "BFS"))
        self.SearchTypecomboBox.setItemText(0, _translate("AI Project", "BFS"))
        self.SearchTypecomboBox.setItemText(1, _translate("AI Project", "DFS"))
        self.SearchTypecomboBox.setItemText(2, _translate("AI Project", "A*"))
        self.SearchTypecomboBox.setItemText(3, _translate("AI Project", "UCS"))
        self.SearchTypecomboBox.setItemText(4, _translate("AI Project", "IDS"))
        self.SearchTypecomboBox.setItemText(5, _translate("AI Project", "Bidirect"))
        self.SearchTypecomboBox.setItemText(6, _translate("AI Project", "BESTF"))
        self.SearchTypecomboBox.setItemText(7, _translate("AI Project", "Alpha-Beta"))
        self.GenerateGraphButton.setText(_translate("AI Project", "Generate Graph"))
        self.Node1Label.setText(_translate("AI Project", "Node 1"))
        self.Node2Label.setText(_translate("AI Project", "Node 2"))
        self.EdgeWieghtLabel.setText(_translate("AI Project", "Edge Wieght"))
        self.AddNodesButton.setText(_translate("AI Project", "Add Nodes"))
        self.TheResult_Label.setWhatsThis(_translate("AI Project",
                                                     "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.GeneratePathButton.setText(_translate("AI Project", "Generate Path"))
        self.TheResultLabel.setText(_translate("AI Project", "The Result"))
        self.NodeLabel.setText(_translate("AI Project", "Node "))
        self.NodeHeuristicLabel.setText(_translate("AI Project", "Node Heuristic"))
        self.AddNodeHeuristicButton.setText(_translate("AI Project", "Add Node Heuristic"))
        self.StartNodeLabel.setText(_translate("AI Project", "Start Node"))
        self.GoalNodeLabel.setText(_translate("AI Project", "Goal Nodes"))
        self.GraphTypecomboBox.setCurrentText(_translate("AI Project", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(0, _translate("AI Project", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(1, _translate("AI Project", "Directed Graph"))
        self.SubmitButton.setText(_translate("AI Project", "Submit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AISearchingTechniquesMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())