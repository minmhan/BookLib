# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 22:46:47 2016

@author: minmhan
"""


from pymongo import MongoClient

class Category:
    business_money = {
        'Accounting':{},
        'Biography & History':{},
        'Business Culture':{},
        'Economics':{},
        'Education & Reference':{},
        'Finance':{},
        'Human Resources':{},
        'Industries':{},
        'Insurance':{},
        'International':{},
        'Investing':{},
        'Job Hunting & Careers':{},
        'Management & Leadership':{},
        'Personal Finance':{},
        'Process & Infrastructure':{},
        'Real Estate':{},
        'Skills':{},
        'Small Business & Entrepreneurship':{},
        'Taxation':{},
        'Women & Business':{}   
    }
    medical = {
        'Administration & Medicine Economics':{},
        'Allied Health Professions':{},
        'Basic Sciences':{},
        'Dentistry':{},
        'History':{},
        'Medical Informatics':{},
        'Medicine':{},
        'Nursing':{},
        'Pharmacology':{},
        'Psychology':{},
        'Research':{},
        'Veterinary Medicine':{}    
    }
    computers_technology = {
        'Business Technology':{
            'Computer & Technology Industry':{},
            'Management Information Systems':{},
            'Microsoft Project':{},
            'Search Engine Optimization':{},
            'SharePoint':{},
            'Social Media for Business':{},
            'Software':{},
            'Web Marketing':{},
            'Window Server':{}        
            },
        'Certification':{
            'Adobe':{},
            'Cisco':{},
            'CompTIA':{},
            'Linux':{},
            'Microsoft':{},
            'Oracle':{},
            'Security':{}
            },
        'Computer Science':{
            'AI & Machine Learning':{'Computer Vision & Pattern Recognition':{}, 'Expert Systems':{},'Intelligence & Semantics':{},
                                     'Machine Theory':{},'Natural Language Processing':{},'Neural Networks':{}}, 
            'Bioinformatics':{},
            'Computer Simulation':{}, 
            'Cybernetics':{},
            'Human-Computer Interaction':{},
            'Information Theory':{},
            'Robotics':{},
            'Systems Analysis & Design':{}
            },
        'Databases & Big Data':{
            'Access':{},
            'Data Mining':{},
            'Data Modeling & Design':{},
            'Data Processing':{},
            'Data Warehousing':{},
            'MySQL':{},
            'Oracle':{},
            'Other Databases':{},
            'Relational Databases':{},
            'SQL':{}
            },
        'Digital Audio, Video & Photography':{},
        'Games & Strategy Guides':{},
        'Graphics & Design':{},
        'Hardware & DIY':{'3D Printing':{},'Design & Architecture':{},'Internet & Networking':{}, 'Mainframes & Minicomputers':{},'Maintenance, Repair & Upgrading':{}, 'Microprocessors &System Design':{},'Peripherals':{},'Personal Computers':{}, 'Robotics':{},'Single Board Computers':{}},
        'History & Culture':{},
        'Internet & Social Media':{},
        'Mobile Phones, Tablets & E-Readers':{
            'Android':{},
            'E-Readers':{},
            'Handheld & Mobile Devices':{},
            'iPad':{},
            'iPhone':{},
            'Programming & App Development':{},
            'Tablets':{}
            },
        'Networking & Cloud Computing':{
            'Cloud Computing':{'Cloud Computing':{},'Data in the Enterprise':{},'Home Networks':{},'Intranets & Extranets':{},'Network Administration':{},'Network Security':{},'Networks Protocols & APIs':{}, 'Wireless Networks':{}},
            'Data in Enterprise':{'Client-Server Systems':{},'Electronic Data Interchange (EDI)':{},'SAP R3':{}},
            'Home Networks':{},
            'Internet, Groupware, & Telecommunications':{},
            'Intranets & Extranets':{},
            'Network Administration':{},
            'Network Security':{},
            'Networks, Protocols & APIs':{},
            'Wireless Networks':{}
            },
        'Operating Systems':{
            'Android':{},
            'BSD':{},
            'Linux':{},
            'Macintosh':{},
            'Solaris':{},
            'Unix':{},
            'Windows':{}
            },
        'Programming':{
            'APIs & Operating Environments':{}, 
            'Algorithms':{'Data Structures':{},'Genetic':{},'Memory Management':{}}, 
            'Apple Programming':{}, 
            'Cross-platform Development':{}, 
            'Functional':{},
            'Game Programming':{}, 
            'Graphics & Multimedia':{}, 
            'Introductory & Beginning':{}, 
            'Languages & Tools':{},
            'Microsoft Programming':{'.NET':{},'C & C++ Windows Programming':{},'SQL Server':{},'VBA':{},'Visual Basic':{}}, 
            'Mobile Apps':{},
            'Parallel Programming':{},
            'Software Design, Testing & Engineering':{},
            'Web Programming':{}
            },
        'Programming Languages':{
            'Ada':{},
            'Ajax':{},
            'Assembly Language Programming':{}, 
            'Boland Delphi':{}, 
            'C & C++':{}, 
            'C#':{}, 
            'CSS':{}, 
            'Compiler Design':{}, 
            'Compilers':{}, 
            'DHTML':{}, 
            'Debugging':{}, 
            'Delphi':{},
            'Fortran':{},
            'Java':{},
            'Lisp':{},
            'Perl':{},
            'Prolog':{},
            'Python':{},
            'RPG':{},
            'Ruby':{},
            'Swift':{},
            'Visual Basic':{},
            'XHTML':{},
            'XML':{},
            'XSL':{},
            'R':{}
            },
        'Security & Encryption':{
            'Cryptography':{},
            'Encryption':{},
            'Hacking':{},
            'Network Security':{},
            'Privacy & Online Safety':{},
            'Security Certifications':{},
            'Viruses':{}   
            },
        'Software':{
            'Accounting':{},
            'Adobe':{},
            'Databases':{},
            'Design & Graphics':{},
            'E-mail':{},
            'Enterprise Applications':{},
            'Mathematical & Statistical':{},
            'Microsoft':{},
            'Optical Character Recognition':{},
            'Personal Finance':{},
            'Presentation Software':{},
            'Project Management Software':{},
            'Quickbooks':{},
            'Spreadsheets':{},
            'Suites':{},
            'Utilities':{},
            'Voice Recognition':{},
            'Word Processing':{}        
        },
        'Web Development & Design':{
            'Content Management':{},
            'Programming':{'ActiveX':{},'ASP.NET':{},'Cold Fusion':{},'CSS':{},'DHTML':{},'Java Server Pages':{},'JavaScript':{},'PHP':{},'Python':{},'Ruby':{},'XSL':{}},
            'User Experience & Usability':{},
            'User Generated Content':{},
            'Web Design':{},
            'Web Marketing':{},
            'Web Services':{},
            'Website Analytics':{}        
            }
        }
    
    #Science and Math
    science_math = {
        'Agricultral Sciences':{},
        'Archaeology':{},
        'Astronomy & Space Science':{},
        'Behavioral Sciences':{},
        'Biological Sciences':{},
        'Chemistry':{},
        'Earth Sciences':{},
        'Environment':{},
        'Essays & Commentary':{},
        'Evolution':{},
        'Experiments, Instruments & Measurement':{},
        'History & Philosophy':{},
        'Mathematics':{          
            'Applied':{
            'Biomathematics':{},
            'Differential Equations':{},
            'Game Theory':{},
            'Graph Theory':{},
            'Linear Programming':{},
            'Probability & Statistics':{},
            'Statistics':{},
            'Stochastic Modeling':{},
            'Vector Analysis':{}            
            },
            'Geometry & Topology':{
                'Algebraic Geometry':{},
                'Analytic Geometry':{},
                'Differential Geometry':{},
                'Non-Euclidean Geometries':{},
                'Topology':{}            
            },
            'History':{},
            'Infinity':{},
            'Mathematical Analysis':{},
            'Matrices':{},
            'Number Systems':{},
            'Popular & Elementary':{},
            'Pure Mathematics':{
                'Algebra':{},
                'Calculus':{},
                'Combinatorics':{},
                'Discrete Mathematics':{},
                'Finite Mathematics':{},
                'Fractals':{},
                'Functional Analysis':{},
                'Group Theory':{},
                'Logic':{},
                'Number Theory':{},
                'Set Theory':{}            
            },
            'Reference':{},
            'Research':{},
            'Study & Teaching':{},
            'Transformations':{},
            'Trigonometry':{}
           },
        'Nature & Ecology':{},
        'Physics':{          
            'Acoustics & Sound':{},
            'Applied':{},
            'Astrophysics':{},
            'Biophysics':{},
            'Chaos Theory':{},
            'Chemical Physics':{},
            'Cosmology':{},
            'Dynamics':{},
            'Electromagnetism':{},
            'Electron Microsocopy':{},
            'Energy':{},
            'Engineering':{},
            'Entropy':{},
            'Gas Mechanics':{},
            'Geophysics':{},
            'Gravity':{},
            'Light':{},
            'Mathematical Physics':{},
            'Mechanics':{},
            'Microscopy':{},
            'Nanostructures':{},
            'Nuclear Physics':{},
            'Optics':{},
            'Quantum Chemistry':{},
            'Quantum Theory':{},
            'Relativity':{},
            'Solid-State Physics':{},
            'System Theory':{},
            'Time':{},
            'Waves & Wave Mechanics':{}
            },
        'Reference':{},
        'Research':{},
        'Science for Kids':{},
        'Technology':{}
    }
    arts_photography={}
    biographies_memoirs={}
    calendars={}
    children_book={}
    christian_bibles={}
    comics_graphicsnovels={}
    cookbooks_food_wine={}
    crafts_hobbies={}
    education_teaching={}
    engineering_transportation={
        'Automotive':{},
        'Engineering':{
            'Aerospace':{},
            'Automotive':{},
            'Bioengineering':{},
            'Chemical':{},
            'Civil & Environmental':{},
            'Computer Modelling':{},
            'Construction':{},
            'Design':{},
            'Electrical & Electronics':{'Circuits':{},'Digital Design':{},'Electric Machinery & Motors':{},'Electronics':{},'Fiber Optics':{},'Networks':{},'Superconductivity':{}},
            'Energy Production & Extraction':{},
            'Industrial, Manufacturing & Operational Systems':{},
            'Marine Engineering':{},
            'Materials & Material Science':{},
            'Mechanical':{},
            'Military Technology':{},
            'Reference':{},
            'Telecommunications & Sensors':{}
        },
        'Transportation':{}
        }
    health_fitness_dieting={}
    history={'Africa':{},'Americas':{},'Arctic & Antarctica':{},'Asia':{},'Australia & Oceania':{},'Europe':{},'Middle East':{},'Russia':{},'United States':{},'World':{},'Ancient Civilizations':{},'Military':{},'Historical Study & Educational Resources':{}}
    humar_entertainment={}
    law={}
    literature_fiction={}
    mystery_thriller_suspense={}
    parenting_relationships={}
    politics_socialsciences={}
    reference={}
    religion_spirituality={}
    romance={}
    
    sciencefiction_fantasy={}
    selfhelp={}
    sports_outdoors={}
    teen_youngadult={}
    test_preparation={}
    travel={}
    
    books = {
        'Arts & Photography': arts_photography,
        'Biographies & Memoirs' : biographies_memoirs,
        'Business & Money': business_money,
        'Calendars': calendars,
        "Children's Books": children_book,
        'Christian Books & Bibles':christian_bibles,
        'Comics & Graphics Novels':comics_graphicsnovels,
        'Computer & Technology':computers_technology,
        'Cookbooks, Food & Wine':cookbooks_food_wine,
        'Crafts, Hobbies & Home':crafts_hobbies,
        'Education & Teaching':education_teaching,
        'Engineering & Transportation':engineering_transportation,
        'Health, Fitness & Dieting':health_fitness_dieting,
        'History':history,
        'Humor & Entertainment':humar_entertainment,
        'Law':law,
        'Literature & Fiction':literature_fiction,
        'Medical Books':medical,
        'Mystery, Thriller & Suspense':mystery_thriller_suspense,
        'Parenting & Relationships':parenting_relationships,
        'Politics & Social Sciences':politics_socialsciences,
        'Reference':reference,
        'Religion & Spirituality':religion_spirituality,
        'Romance':romance,
        'Science & Math':science_math,
        'Science Fiction & Fantasy':sciencefiction_fantasy,
        'Self-Help':selfhelp,
        'Sports & Outdoors':sports_outdoors,
        'Teen & Young Adult':teen_youngadult,
        'Test Preparation':test_preparation,
        'Travel':travel
    }
    
    db = None
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client.ebooks
    
    def create(self):
        if self.db.categories.find({'_id':'Books'}).count() == 0:
            self.db.categories.insert_one({'_id': 'Books', 'ancestors': [], 'parent': None})
        
        self.create_childs(self.books,['Books'],'Books')


    
    def create_childs(self, category, ancestors, parent):
        for k,v in category.items():
            if len(v.keys()) > 0:
                ans = list(ancestors)
                ans.append(k) 
                if self.db.categories.find({'_id':k}).count() == 0:
                    self.db.categories.insert_one({'_id':k, 'ancestors':ancestors, 'parent': parent})
                self.create_childs(v,ans, k)
            else:
                if self.db.categories.find({'_id':k}).count() == 0:                    
                    self.db.categories.insert_one({'_id':k, 'ancestors':ancestors, 'parent': parent})
                
        
        
    def delete(self):
        pass
    
    def isexist(self,category):
        return self.db.categories.find({'_id':category}).count() > 0
        
    
    
cat = Category()
cat.create()
print(cat.isexist('Electronics'))