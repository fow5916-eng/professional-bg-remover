import os
import click
from src.remover import BackgroundRemover
from tqdm import tqdm

@click.command()
@click.option('--input', '-i', required=True, help='Path to input image or directory.')
@click.option('--output', '-o', help='Path to output directory. Defaults to "output" folder.')
def main(input, output):
    """
    🚀 Image Background Remover CLI
    A professional tool to remove backgrounds from images using AI.
    """
    if not output:
        output = 'output'

    if os.path.isfile(input):
        click.echo(f"Processing single image: {input}...")
        if not os.path.exists(output):
            os.makedirs(output)
            
        output_path = os.path.join(output, os.path.splitext(os.path.basename(input))[0] + ".png")
        if BackgroundRemover.remove_background(input, output_path):
            click.secho(f"✅ Success! Saved to: {output_path}", fg='green')
        else:
            click.secho("❌ Failed to process image.", fg='red')
            
    elif os.path.isdir(input):
        click.echo(f"Batch processing directory: {input}...")
        supported_extensions = ('.jpg', '.jpeg', '.png', '.webp')
        files = [f for f in os.listdir(input) if f.lower().endswith(supported_extensions)]
        
        if not files:
            click.secho("No supported images found in directory.", fg='yellow')
            return

        with tqdm(total=len(files), desc="Processing") as pbar:
            results = BackgroundRemover.batch_process(input, output)
            pbar.update(len(files))
            
        success_count = sum(1 for _, success in results if success)
        click.secho(f"\n✨ Batch process complete!", bold=True)
        click.echo(f"Successfully processed: {success_count}/{len(files)}")
        click.echo(f"Files saved in: {os.path.abspath(output)}")
        
    else:
        click.secho(f"Invalid input path: {input}", fg='red')

if __name__ == '__main__':
    main()
