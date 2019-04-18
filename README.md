# csv2txt
Simple tool to convert CSV lines into Markdown texts.

## Version

1.0 - by zelacerda

## Usage

`
python csv2txt.py src dest
`

Where `src` points to a CSV file and `dest` points to an output Markdown file.

The first column is always used as a H2 header.

## Output example

A CSV file like this:

|Nome          |idade          |cidade        |profissão     |
|--------------|---------------|--------------|--------------|
|João          |42             |Jundiaí       |Jornalista    |
|Maria         |45             |Florianópolis |Médico        |
|Miguel        |34             |Jundiaí       |Engenheiro    |
|Paula         |42             |São Paulo     |Médico        |

will have the following output:


\## João

\**idade**: 42

\**cidade**: Jundiaí

\**profissão**: Jornalista

\## Maria

\**idade**: 45

\**cidade**: Florianópolis

\**profissão**: Médico

\## Miguel

\**idade**: 34

\**cidade**: Jundiaí

\**profissão**: Engenheiro

\## Paula

\**idade**: 42

\**cidade**: São Paulo

\**profissão**: Médico

