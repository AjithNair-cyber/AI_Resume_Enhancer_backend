class Resume:
    def __init__(
        self,
        user_id : str,
        name: str,
        job_role: str,
        mobile: str,
        email: str,
        linkedin: str,
        github: str,
        professional_summary: str,
        key_skills: list,
        experience: list,
        projects: list,
        education: list,
        certifications: list,
        hobbies: list,
        languages: list
    ):
        self.name = name
        self.job_role = job_role
        self.mobile = mobile
        self.email = email
        self.linkedin = linkedin
        self.github = github
        self.professional_summary = professional_summary
        self.key_skills = key_skills
        self.experience = experience
        self.projects = projects
        self.education = education
        self.certifications = certifications
        self.hobbies = hobbies
        self.languages = languages

    def get_resume(self) -> dict:
        return {
            "name": self.name,
            "job_role": self.job_role,
            "mobile": self.mobile,
            "email": self.email,
            "linkedin": self.linkedin,
            "github": self.github,
            "professional_summary": self.professional_summary,
            "key_skills": self.key_skills,
            "experience": self.experience,
            "projects": self.projects,
            "education": self.education,
            "certifications": self.certifications,
            "hobbies": self.hobbies,
            "languages": self.languages,
        }
