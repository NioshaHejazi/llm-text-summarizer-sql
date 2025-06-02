import typer
import csv
from app.summarizer import summarize
from app.database import init_db, insert_summary
from typing import Optional
from app.database import get_connection
from pathlib import Path


app = typer.Typer()

@app.command("summarize-text")
def summarize_text(
    input: Optional[str] = typer.Option(None, "--input", help="Text to summarize."),
    file: Optional[Path] = typer.Option(None, "--file", help="Path to text file."),
    tags: Optional[str] = typer.Option(None, "--tags", help="Comma-separated tags."),
):
    """Summarize input text from CLI or file and store in DB."""
    if input:
        text = input
    elif file:
        if file.exists():
            text = file.read_text()
        else:
            typer.echo("❌ File not found.")
            raise typer.Exit()
    else:
        typer.echo("❌ Please provide either --input or --file.")
        raise typer.Exit()

    summary = summarize(text)
    insert_summary(text, summary, tags)
    typer.echo("\n✅ Summary saved to database:\n")
    typer.echo(summary)


@app.command("list")
def list_summaries(limit: int = 5):
    """List the most recent summaries."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, input_text, summary_text, tags, created_at
        FROM summaries
        ORDER BY created_at DESC
        LIMIT %s;
    """, (limit,))
    rows = cursor.fetchall()

    if not rows:
        print("❌ No summaries found.")
        return

    for row in rows:
        print(f"\n📄 ID: {row['id']}")
        print(f"🕓 Date: {row['created_at']}")
        print(f"🏷️ Tags: {row['tags']}")
        print(f"📝 Summary: {row['summary_text'][:150]}...\n")

@app.command("search")
def search_summaries(keyword: str):
    """Search summaries containing a keyword."""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT id, input_text, summary_text AS summary, tags, created_at
        FROM summaries
        WHERE input_text ILIKE %s OR summary_text ILIKE %s OR tags ILIKE %s
        ORDER BY created_at DESC;
    """
    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    rows = cursor.fetchall()

    if not rows:
        typer.echo("❌ No matching summaries found.")
        return

    for row in rows:
        typer.echo(f"\n📄 ID: {row['id']}")
        typer.echo(f"🕓 Date: {row['created_at']}")
        typer.echo(f"🏷️ Tags: {row['tags']}")
        typer.echo(f"📝 Summary: {row['summary'][:150]}...\n")


@app.command("export")
def export_summaries(output_path: str = "summaries.csv"):
    """Export all summaries to a CSV file."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, input_text, summary_text AS summary, tags, created_at
        FROM summaries
        ORDER BY created_at DESC;
    """)
    rows = cursor.fetchall()

    if not rows:
        typer.echo("❌ No summaries to export.")
        return

    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Input Text", "Summary", "Tags", "Created At"])
        for row in rows:
            writer.writerow([row["id"], row["input_text"], row["summary"], row["tags"], row["created_at"]])
    typer.echo(f"✅ Exported {len(rows)} summaries to {output_path}")




@app.command()
def init():
    """Initialize the database (create tables)."""
    init_db()
    typer.echo("✅ Database initialized.")

if __name__ == "__main__":
    app()
