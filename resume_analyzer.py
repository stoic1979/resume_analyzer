#
# main class for anayzing a resume and dumping the resume features in database
#

#from exceptions import InvalidResumeException


class ResumeAnalyzer:


    def __init__(self, resume_path):
        self.resume_path = resume_path

        # read resume
        self.validate_resume()


    def validate_resume(self):
        print "[ResumeAnalyzer] :: validation resume..."

        #TODO
        # ensure that resume is valid or throw exception



        #FIXME - remove it
        #raise InvalidResumeException("Invalid resume, format should be .doc or .docx")


    def process_resume(self):
        print "[ResumeAnalyzer] :: processing resume..."


if __name__ == "__main__":
    ra = ResumeAnalyzer("./samples/resume1.doc")
    ra.process_resume()
