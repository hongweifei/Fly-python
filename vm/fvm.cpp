




#include "fvm.hpp"
#include <stdlib.h>



void fvm_open(FlyVM *vm,std::string file_name)
{
    vm->file_name = file_name;
    FILE *fp = vm->fp = fopen(file_name.c_str(),"r");

    while (1)
    {
        fvm_read_order(vm);

    }
    
}



void fvm_read_order(FlyVM *vm)
{
    vm->last_order = vm->order;
    fread(&vm->order,sizeof(int),1,vm->fp);
}



void fvm_run_order(FlyVM *vm)
{
    int var_index;
    

    switch (vm->order)
    {
    case VAR_NUMBER:
        double d;

        fread(&var_index,sizeof(int),1,vm->fp);
        fread(&d,sizeof(double),1,vm->fp);

        vm->number.insert(std::map<int, double>::value_type (var_index, d));
        break;
    case VAR_BOOLEAN:
        break;
    case VAR_CHAR:
        char ch;

        fread(&var_index,sizeof(int),1,vm->fp);
        fread(&ch,sizeof(char),1,vm->fp);

        vm->ch.insert(std::map<int, char>::value_type (var_index, ch));
        break;
    case VAR_STRING:
        std::string str;
        break;
    case VAR_UNION:
        FUnion *fu;
        break;
    case VAR_STRUCT:
        FStruct *fs;
        break;
    case VAR_CLASS:
        FClass *fc;
        break;


    case VAR_CHANG_VALUE:
        break;

    case VAR_ADD:
        break;

    case VAR_TO_STRING:
        break;

    case VAR_SWAP:
        break;

    case PRINT:
        int n = 0;
        char *text;

        fread(&n,sizeof(int),1,vm->fp);
        fread(text,sizeof(char),n,vm->fp);
        printf("%s",text);
        break;
    
    default:
        break;
    }
}










