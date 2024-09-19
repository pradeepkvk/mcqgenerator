from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='sunny savita',
    author_email='sunny.savita@ineuron.ai',
    install_requires=["langchain_groq","langchain","streamlit","python-dotenv","PyPDF2","ipykernel"],
    packages=find_packages()
)