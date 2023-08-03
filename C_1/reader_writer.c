/* this code is not compiled  as i dont have environment available */
#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>


//N writers and M readers

#define M 10  //Readers
#define N 20  //Writer

sem_t mutex;
sem_t db;
int reader_count = 0;


void *reader_thread(void *arg) {
	
	while(1) {
		sem_wait(&mutex);
		reader_count++;
		if (reader_count >0) {
			sem_wait(&db);
		}
		if (reader_count <= M) {
			sem_post(&mutex);  //allow M number of readers 
		}
		else{
			sem_wait(&mutex);  //lock if readers count is reached to M
		}
		printf("Reader is Reading");  //reads task is in proggress
		reader_count--;    
		if (reader_count ==0){
			sem_post(&db);
		}
		sem_post(&mutex);  //release reader
			
	}
	return NULL;
}

void *writer_thread(void *arg) {
	//TODO: Define set-up required
	while(1) {
		sem_wait(&db);  //Write lock acquired
		printf("writer is writing");  //Writing task in progress
		sem_post(&db);  //Releasing write lock
	}
	return NULL;
}



int main(int argc, char **argv) {
	int i;
	for(i = 0; i < N; i++) {
		pthread_create(NULL, NULL, reader_thread, NULL);
		}
		
	for(i = 0; i < M; i++) {
		pthread_create(NULL, NULL, writer_thread, NULL);
		}
	
	return 0;
}
