


#include <stdio.h>
#include <map>
#include <string>

#ifndef __FVM_HEAD__
#define __FVM_HEAD__


typedef enum : int
{
    NONE = 0,
};


typedef enum : int
{
    /*定义*/
    CREATE_UNION = 0x128,
    CREATE_STRUCT,
    CREATE_CLASS,

    /*声明变量*/
    VAR_NUMBER,
    VAR_BOOLEAN,
    VAR_CHAR,
    VAR_STRING,
    VAR_UNION,
    VAR_STRUCT,
    VAR_CLASS,

    /***/
    VAR_CHANG_VALUE,
    VAR_ADD,
    VAR_TO_STRING,
    VAR_SWAP,
} Variable;



typedef enum : int
{
    STR_ADD = 0x256,
    STR_LEN,
} Str;


typedef enum : int
{
    PRINT = 0x512,
} Funtion;




typedef struct
{
    
} FUnion;


typedef struct
{
    
} FStruct;


typedef struct
{
    
} FClass;


typedef struct FlyVM
{
    std::string file_name;
    FILE *fp;
    unsigned long long offset;

    int last_order;
    int order;

    
    
    //std::map<int,long> l;
    std::map<int,double> number;
    std::map<int,bool> boolean;
    std::map<int,char> ch;
    std::map<int,std::string> str;
    std::map<int,FUnion> user_union;
    std::map<int,FStruct*> user_struct;
    std::map<int,FClass*> user_class;



} FlyVM;



void fvm_open(FlyVM*,std::string);


void fvm_read_order(FlyVM*);
void fvm_run_order(FlyVM*);


#endif // __FVM_HEAD__






