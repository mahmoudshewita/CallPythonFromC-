using Python.Runtime;


Runtime.PythonDLL = @"C:\Python312\python312.dll";
PythonEngine.Initialize();
using (Py.GIL())
{
    // python file name without .py extenssion
    var pyScript = Py.Import("pdf_text_extractor");

    // call pthon function without parameter
    var res = pyScript.InvokeMethod("hello");
    Console.WriteLine(res);

    // call pthon function with parameter
    var PDFfilePath_PyFunctionParameter = new PyString("test.pdf");
    var PDFTextResult = pyScript.InvokeMethod("extractTextFromPDF", new PyObject[] { PDFfilePath_PyFunctionParameter });
    Console.Write(PDFTextResult);

}