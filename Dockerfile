FROM python
WORKDIR project/
COPY . .
RUN python -m pip install --upgrade pip 
RUN pip install flask pymysql

EXPOSE 4000

ENTRYPOINT ["python"]
CMD ["myapp.py"]

#HEALTHCHECK --inverval=30s --timeout=10s --retries=3 CMD curl -fail http://localhost:4000 || exit 1

